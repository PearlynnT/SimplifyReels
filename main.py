from services.image_service import fetch_images, download_and_resize_images
from services.video_service import generate_video

if __name__ == "__main__":
    # Step 1: Fetch image URLs using Google Custom Search API
    query = "kyle field"  # Replace with your own query
    image_urls = fetch_images(query, num_results=5)  # Fetch 5 images

    # Step 2: Download the images
    image_paths = download_and_resize_images(image_urls)
    # image_paths = []
    # for idx, image_url in enumerate(image_urls):
    #     print(f"Fetching Image {idx+1}: {image_url}")
    #     download_image(image_url, idx)
    #     image_paths.append(f'./services/image_{idx+1}.jpg')

    # Step 3: Generate a video from the downloaded images
    generate_video(image_paths, output_file="output_video.mp4", duration_per_image=2)
