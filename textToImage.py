from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_path, output_path, font_size=24, image_size=(400, 200), text_color=(0, 0, 0), bg_color=(255, 255, 255)):
    # Create a new image with a white background
    img = Image.new('RGB', image_size, bg_color)
    draw = ImageDraw.Draw(img)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate text position to center it on the image
    text_width, text_height = draw.textsize(text, font)
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=text_color)

    # Save the image
    img.save(output_path)

# Example usage
text = "Hello, Python!"
font_path = "COMIC.ttf"
output_path = "output_image.png"

text_to_image(text, font_path, output_path)
