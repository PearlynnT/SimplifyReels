from services.image_service import fetch_images, download_and_resize_images
from services.video_service import generate_video
from services.subtitle_service import generate_images_from_texts

def read_queries_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Evaluate the string as a Python list
        queries = eval(content)
    return queries

if __name__ == "__main__":
    # Step 1: Read queries from chat_output.txt
    queries = read_queries_from_file('chat_output.txt')

    # Generate images for each query
    generated_image_paths = generate_images_from_texts(queries)

    all_image_paths = []
    
    for idx, query in enumerate(queries):
        # Fetch image URLs using Google Custom Search API for each query
        fetched_image_url = fetch_images(query, num_results=10)

        if fetched_image_url:
            # Add the generated image for the current query
            all_image_paths.append(generated_image_paths[idx])

            # Add the fetched image path (you may need to download it first)
            downloaded_images = download_and_resize_images([fetched_image_url])
            all_image_paths.extend(downloaded_images)

    # Step 3: Generate a video from the combined list of images
    generate_video(all_image_paths, output_file="output_video.mp4", duration_per_image=2)

    # image_urls = []
    # for query in queries:
    #     # Fetch image URLs using Google Custom Search API for each query
    #     image_urls.append(fetch_images(query, num_results=10))

    # # # Step 1: Fetch image URLs using Google Custom Search API
    # # query = "kyle field"  # Replace with your own query
    # # image_urls = fetch_images(query, num_results=1)  # Fetch 5 images

    # # Step 2: Download the images
    # image_paths = download_and_resize_images(image_urls)
    # # image_paths = []
    # # for idx, image_url in enumerate(image_urls):
    # #     print(f"Fetching Image {idx+1}: {image_url}")
    # #     download_image(image_url, idx)
    # #     image_paths.append(f'./services/image_{idx+1}.jpg')

    # # Step 3: Generate a video from the downloaded images
    # generate_video(image_paths, output_file="output_video.mp4", duration_per_image=2)
