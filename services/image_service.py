import os
import requests
from dotenv import load_dotenv, dotenv_values 
from PIL import Image
from io import BytesIO

load_dotenv() 

def is_valid_image(url):
    try:
        # First, try using the HEAD request
        response = requests.head(url, allow_redirects=True)
        # Fallback to GET request if HEAD doesn't return necessary headers
        if "Content-Type" not in response.headers:
            response = requests.get(url, stream=True)  # stream=True to avoid downloading the entire image

        # Safely check for the Content-Type header
        content_type = response.headers.get("Content-Type", "")
        return response.status_code == 200 and "image" in content_type
    except requests.RequestException:
        return False
    # try:
    #     response = requests.head(url, allow_redirects=True)  # Use HEAD request to check if the image exists
    #     return response.status_code == 200 and "image" in response.headers["Content-Type"]
    # except requests.RequestException:
    #     return False

def fetch_images(query, num_results=20):
    search_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": os.getenv("GOOGLE_CUSTOM_SEARCH_API_KEY"),
        "cx": os.getenv("SEARCH_ENGINE_ID"),
        "searchType": "image",
        "num": num_results
    }

    response = requests.get(search_url, params=params)
    search_results = response.json()
    print(search_results)

    valid_image_url = None
    if "items" in search_results:
        for item in search_results["items"]:
            image_url = item["link"]
            # Check if the image URL is valid
            if is_valid_image(image_url):
                valid_image_url = image_url
                break  # Stop at the first valid image

    return valid_image_url

def download_and_resize_images(image_urls, target_size=(1080, 1920), folder="downloaded_images", query_idx=0):
    """
    Downloads and resizes images from the given URLs.

    Args:
        image_urls (list): A list of image URLs.
        target_size (tuple): Target size for the images (default is 1080x1920 pixels).
        output_folder (str): Folder to save the downloaded and resized images.

    Returns:
        list: A list of paths to the downloaded and resized images.
    """

    if not os.path.exists(folder):
        os.makedirs(folder)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    image_paths = []
    for idx, url in enumerate(image_urls):
        print(f"Processing URL {idx + 1}: {url}")
        try:
            response = requests.get(url, headers=headers)
            
            # Check if the request was successful
            if response.status_code != 200:
                print(f"Failed to retrieve image {idx+1} from {url} (Status code: {response.status_code})")
                continue

            # Validate the content type to ensure it's an image
            content_type = response.headers['Content-Type']
            if not content_type.startswith('image'):
                print(f"URL {url} did not return an image (Content-Type: {content_type})")
                continue

            # Open the image
            img = Image.open(BytesIO(response.content))

            # Convert RGBA to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            # Get original dimensions
            original_width, original_height = img.size

            # Calculate scaling factors
            scale_x = target_size[0] / original_width
            scale_y = target_size[1] / original_height
            scale = max(scale_x, scale_y)  # Use the larger scaling factor to fill the target size

            # Calculate new dimensions
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)

            # Resize the image while maintaining aspect ratio
            img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Create a new blank image with the target size and paste the resized image onto it
            new_img = Image.new("RGB", target_size, (255, 255, 255))  # White background
            img_width, img_height = img.size
            x = (target_size[0] - img_width) // 2
            y = (target_size[1] - img_height) // 2
            new_img.paste(img, (x, y))
            
            img_path = os.path.join(folder, f"query_{query_idx}_image_{idx+1}.jpg")
            new_img.save(img_path)
            image_paths.append(img_path)
            print(f"Downloaded and resized image: {url}")

        except requests.RequestException as e:
            print(f"Failed to download image {url}: {e}")
        except Exception as e:
            print(f"Failed to process image {url}: {e}")
    
    return image_paths
