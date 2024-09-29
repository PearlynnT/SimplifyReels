from services.image_service import fetch_images, download_and_resize_images
from services.video_service import generate_video
from services.subtitle_service import generate_images_from_texts
# import ast
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# def preprocess_string(string):
#     string = string.replace('"', '\\"')
#     return string

def read_queries_from_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        first_list = json.loads(content[0].strip())
        second_list = json.loads(content[1].strip())
        # first_list = json.loads(preprocess_string(content[0].strip()))
        # second_list = json.loads(preprocess_string(content[1].strip()))
        # first_list = ast.literal_eval(content[0].strip()) 
        # second_list = ast.literal_eval(content[1].strip())
    return first_list, second_list

def generate_video_from_queries():
    # Step 1: Read queries from chat_output.txt
    first_list, second_list = read_queries_from_file('chat_output.txt')

    # Ensure the lists are not empty and of the same length
    if not first_list or not second_list:
        print("Query lists are empty or missing.")
        return

    if len(first_list) != len(second_list):
        print("Mismatch between the lengths of first and second lists.")
        return

    # Step 2: Generate images for each query in the first list
    generated_image_paths = generate_images_from_texts(first_list)
    
    if not generated_image_paths or len(generated_image_paths) != len(first_list):
        print("Failed to generate images for queries.")
        return

    all_image_paths = []
    
    # Fetch images for the second list of queries
    for idx, query in enumerate(second_list):
        try:
            fetched_image_url = fetch_images(query, num_results=10)
            if fetched_image_url is None:
                print("no url")
            
            if fetched_image_url:
                # Add the generated image for the current query
                all_image_paths.append(generated_image_paths[idx])

                # Download the fetched image and resize it
                downloaded_images = download_and_resize_images([fetched_image_url], query_idx=idx)
                all_image_paths.extend(downloaded_images)

        except Exception as e:
            print(f"Error processing query {query}: {e}")

    # Ensure we have some images to create a video
    if not all_image_paths:
        print("No images found to create the video.")
        return

    # Step 3: Generate a video from the combined list of images
    try:
        generate_video(all_image_paths, output_file="output_video.mp4", duration_per_image=2)
        print("Video generated successfully.")
    except Exception as e:
        print(f"Error generating video: {e}")

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("chat_output.txt"):
            print(f"{event.src_path} has been modified. Generating video...")
            generate_video_from_queries()

if __name__ == "__main__":
    # Set up the observer
    path = "."
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    # Start the observer
    try:
        observer.start()
        print(f"Watching for changes in {path}/chat_output.txt...")
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
