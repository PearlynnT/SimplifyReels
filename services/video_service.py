from moviepy.editor import ImageClip, concatenate_videoclips

def generate_video(image_paths, output_file="output_video.mp4", duration_per_image=2):
    clips = []
    for img_path in image_paths:
        # Create a clip for each image, with the specified duration
        clip = ImageClip(img_path).set_duration(duration_per_image)
        clips.append(clip)
    
    # Concatenate all image clips into one video
    video = concatenate_videoclips(clips, method="compose")
    
    # Write the final video file
    video.write_videofile(output_file, fps=24)
    