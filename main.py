from services.image_service import fetch_images, download_and_resize_images
from services.video_service import generate_video
from services.subtitle_service import generate_images_from_texts
import ast

def read_queries_from_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        first_list = ast.literal_eval(content[0].strip()) 
        second_list = ast.literal_eval(content[1].strip())
    return first_list, second_list

if __name__ == "__main__":
    # Step 1: Read queries from chat_output.txt
    first_list, second_list = read_queries_from_file('chat_output.txt')

    # Generate images for each query in the first list
    generated_image_paths = generate_images_from_texts(first_list)

    all_image_paths = []
    for idx, query in enumerate(second_list):
        fetched_image_url = fetch_images(query, num_results=10)

        if fetched_image_url:
            # Add the generated image for the current query
            all_image_paths.append(generated_image_paths[idx])

            # Add the fetched image path (you may need to download it first)
            downloaded_images = download_and_resize_images([fetched_image_url], query_idx=idx)
            all_image_paths.extend(downloaded_images)

    # Step 3: Generate a video from the combined list of images
    generate_video(all_image_paths, output_file="output_video.mp4", duration_per_image=2)
