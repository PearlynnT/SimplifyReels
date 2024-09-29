from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont
import os

def generate_image_with_text(text, output_path, image_size=(1080, 1920), font_size=50):
    # Create a new blank image with white background
    img = Image.new('RGB', image_size, color=(255, 255, 255))
    
    # Load a font (you can specify your own .ttf font file)
    try:
        font = font_manager.FontProperties(family='sans-serif', weight='regular')
        file = font_manager.findfont(font)
        font = ImageFont.truetype(file, font_size)  # Adjust the font and size as needed
    except IOError:
        print("TTF font not found. Using default bitmap font, which doesn't support size scaling.")
        font = ImageFont.load_default()  # Use default font if the specified font is not found

    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    # Calculate text size and position
    # text_bbox = draw.textbbox((0, 0), text, font=font)
    # text_width = text_bbox[2] - text_bbox[0]  # bbox: (left, top, right, bottom)
    # text_height = text_bbox[3] - text_bbox[1]

    # Adjust the font size until the text fits within the image bounds
    while True:
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Check if text fits within the image with a margin
        if text_width <= image_size[0] * 0.9 and text_height <= image_size[1] * 0.9:
            break
        else:
            # Decrease the font size
            font_size = font.size - 10
            if font_size <= 10:  # Ensure font size doesn't get too small
                print("Font size is too small, stopping resizing.")
                break
            font = ImageFont.truetype(file, font_size)

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
