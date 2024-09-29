from PIL import Image, ImageDraw, ImageFont
import os

def generate_image_with_text(text, output_path, image_size=(1080, 1920), font_size=500):
    # Create a new blank image with white background
    img = Image.new('RGB', image_size, color=(255, 255, 255))
    
    # Load a font (you can specify your own .ttf font file)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Adjust the font and size as needed
    except IOError:
        font = ImageFont.load_default()  # Use default font if the specified font is not found

    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # bbox: (left, top, right, bottom)
    text_height = text_bbox[3] - text_bbox[1]

    text_x = (image_size[0] - text_width) / 2
    text_y = (image_size[1] - text_height) / 2
    
    # Draw the text onto the image
    draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)  # Black text
    
    # Save the image
    img.save(output_path)

def generate_images_from_texts(texts, output_folder="generated_images"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    generated_images = []
    for idx, text in enumerate(texts):
        output_path = os.path.join(output_folder, f"text_image_{idx + 1}.png")
        generate_image_with_text(text, output_path)
        generated_images.append(output_path)
        print(f"Generated image for: {text}")
    return generated_images
