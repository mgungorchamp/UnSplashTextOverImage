from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
import requests
import random
import string
from PIL import Image, ImageDraw, ImageFont

# Function to fetch a random image URL from Unsplash
def get_random_image_url(url):
    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for any HTTP error
        return response.url
    except Exception as e:
        print(f"Error fetching random image: {e}")
        return None

# URL for random images from Unsplash with specified categories and size
#url = "https://source.unsplash.com/random/1920x1080/?wallpaper,landscape,animals,flowers,forest,abstract-wallpaper"

# Get a random image URL
#random_image_url = get_random_image_url(url)

# Print the URL
#print("Random image URL:", random_image_url)

# Function to download an image from a URL and save it to a file
def download_image(url, file_path):
    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for any HTTP error
        
        # Open the file in binary write mode and write the image data
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Image downloaded successfully and saved as {file_path}")
    except Exception as e:
        print(f"Error downloading image: {e}")

#create 4 digit random number and convert it to string
def random_4_digit_number():
    return ''.join(random.choices(string.digits, k=4))


def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def add_text_to_image(image_path, text, font_size=30, text_color=(255, 255, 255), margin=50):
    # Open the image
    image = Image.open(image_path)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.load_default()  # You can also load a specific font using ImageFont.truetype()
    
    # Calculate text size and position
    font = ImageFont.truetype("arial.ttf", font_size)

    text_width, text_height = textsize(text, font=font) #draw.textlength(text, font=font)
    #text_length = draw.textlength(text, font=font)
    x = (image.width - text_width) / 2
    y = image.height - text_height - margin
    
    # Add text to the image
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the modified image
    image.save("output.jpg")
    print("Text added to image and saved as output.jpg")

# URL of the image to download
url = "https://source.unsplash.com/random/1920x1080/?wallpaper,landscape,animals,flowers,forest,abstract-wallpaper"


# File path where you want to save the downloaded image
number = random_4_digit_number()
file_path = "image_"+ number +".jpg"  # You can specify any file path and name here
file_output_path = "image_"+ number +"_text.jpg"
# Download the image
download_image(url, file_path)

#add_text_to_image(file_path, "Hello, World!", font_size=50, text_color=(255, 255, 255), margin=100)
'''
def add_text_with_shadow(image_path, text, font_size=30, text_color=(255, 255, 255), shadow_color=(0, 0, 0), shadow_offset=(2, 2), margin=50):
    # Open the image
    image = Image.open(image_path)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.load_default()  # You can also load a specific font using ImageFont.truetype()
    
    # Calculate text size and position
    font = ImageFont.truetype("arial.ttf", font_size)
    #text_width, text_height = draw.textsize(text, font=font)
    text_width, text_height = textsize(text, font=font) #draw.textlength(text, font=font)
    x = (image.width - text_width) / 2
    y = image.height - text_height - margin
    
    # Draw the text with black color (shadow)
    shadow_position = (x + shadow_offset[0], y + shadow_offset[1])
    draw.text(shadow_position, text, fill=shadow_color, font=font)
    
    # Draw the text with white color
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the modified image
    image.save(file_output_path)

add_text_with_shadow(file_path, "Bir insanın okuyup öğrendikleri ne kadar çok olursa olsun, hiçbir zaman onu okuyup-öğrenmekten alıkoymamalıdır. Gerçek ilim adamları, daha çok, sürekli araştırmalarının yanında, bildiklerini yetersiz bulan kimseler arasından çıkmıştır.", font_size=50, text_color=(255, 255, 255), shadow_color=(0, 0, 0), shadow_offset=(2, 2), margin=100)
'''

import textwrap

def add_text_with_shadow(image_path, text, font_size=30, text_color=(255, 255, 255), shadow_color=(0, 0, 0), shadow_offset=(2, 2), margin=50, max_line_width=500):
    # Open the image
    image = Image.open(image_path)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.load_default()  # You can also load a specific font using ImageFont.truetype()
    
    # Calculate text size and position
    font = ImageFont.truetype("arial.ttf", font_size)
    #max_text_width = min(max_line_width, image.width - 2 * margin)
    max_text_width = image.width - 2 * margin
    
    
    # Wrap the text to fit within the maximum line width
    wrapped_text = textwrap.fill(text, width= (max_text_width // font_size) * 2)
    
    # Split the wrapped text into multiple lines
    lines = wrapped_text.split('\n')
    
    # Calculate total text height
    total_text_height = sum(textsize(line, font=font)[1] for line in lines)
    
    # Calculate text position
    x = (image.width - max_text_width) / 2
    y = (image.height - total_text_height) / 7
    
    # Draw the text with black color (shadow) and white color
    for line in lines:
        shadow_position = (x + shadow_offset[0], y + shadow_offset[1])
        draw.text(shadow_position, line, fill=shadow_color, font=font)
        draw.text((x, y), line, fill=text_color, font=font)
        y += textsize(line, font=font)[1]  # Move to the next line
        
    image.save(file_output_path)
    print("Image saved to" + file_output_path)


long_text = "Peace"
add_text_with_shadow(file_path, long_text, font_size=80, text_color=(255, 255, 255), shadow_color=(0, 0, 0), shadow_offset=(2, 2), margin=55)