'''
pip install requests
pip install pillow
'''

from pipes import quote
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
import requests
import random
import string
from PIL import Image, ImageDraw, ImageFilter, ImageFont


#url = "https://source.unsplash.com/random/1920x1080/?cyber"
#url = "https://source.unsplash.com/random/1920x1080/?wallpaper"
#url = "https://source.unsplash.com/random/1920x1080/?wallpaper,landscape,animals,flowers,forest,abstract-wallpaper"
url = "https://source.unsplash.com/random/1920x1080/?islam,flowers,forest,abstract-wallpaper"


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
#url = "https://source.unsplash.com/random/1920x1080/?wallpaper,landscape,animals,flowers,forest,abstract-wallpaper"
#url = "https://source.unsplash.com/random/1920x1080/?computer,software"
#url = "https://source.unsplash.com/random/1920x1080/?wallpaper,landscape,animals,flowers,forest,abstract-wallpaper,computer,software"

# Define the relative path
relative_path = "output/"
import os
# Create the folder structure if it doesn't exist
if not os.path.exists(relative_path):
    os.makedirs(relative_path)


# File path where you want to save the downloaded image
number = random_4_digit_number()
image_name_org = "image_"+ number +".jpg"  # You can specify any file path and name here
image_with_text = "image_"+ number +"_text.jpg"
# Download the image 

# Combine the relative path and file name
file_path = os.path.join(relative_path, image_name_org)
file_path_text = os.path.join(relative_path, image_with_text)

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

def add_text_with_shadow_box(image_path, quote, author, font_size=30, text_color=(255, 255, 255), shadow_color=(0, 0, 0), shadow_offset=(2, 2), margin=50, max_line_width=500):
    # Open the image
    background_image = Image.open(image_path)
    
    # Convert the image to RGBA mode to support transparency
    background_image = background_image.convert("RGBA")
    
    # Create a drawing object
    draw = ImageDraw.Draw(background_image)
    
    # Load a font
    font = ImageFont.load_default()  # You can also load a specific font using ImageFont.truetype()
    
    # Calculate text size and position
    #font = ImageFont.truetype("arial.ttf", font_size)
    #font = ImageFont.truetype("pala.ttf", font_size)
    font = ImageFont.truetype("calibri.ttf", font_size)
    #font = ImageFont.truetype("verdana.ttf", font_size)
    
    #max_text_width = min(max_line_width, image.width - 2 * margin)
    max_text_width = background_image.width - 2 * margin
    
    
    # Wrap the text to fit within the maximum line width
    wrapped_text = textwrap.fill(quote, width=(max_text_width // font_size) * 2.2) #(max_text_width // font_size) * 2)
    
    # Split the wrapped text into multiple lines
    lines = wrapped_text.split('\n')
    
    # Calculate total text height
    total_text_height = sum(textsize(line, font=font)[1] for line in lines)
    
    # Calculate text position
    x = (background_image.width - max_text_width) / 2
    y = (background_image.height - total_text_height) / 7

     # Calculate the size of the transparent text box
    box_width = max_text_width + 2 * margin
    box_height = total_text_height + 4 * margin
    
    # Calculate the coordinates of the transparent text box
    box_x1 = x - margin
    box_y1 = y - margin
    box_x2 = box_x1 + box_width
    box_y2 = box_y1 + box_height
    
    # Draw a transparent rectangle behind the text
    #draw.rectangle([box_x1, box_y1, box_x2, box_y2], fill=(0, 0, 0, 0))  # Adjust the transparency as needed
    # Create a separate image for the transparent rectangle
    rect_image = Image.new("RGBA", background_image.size, (0, 0, 0, 0))
    rect_draw = ImageDraw.Draw(rect_image)
    rect_draw.rectangle([box_x1, box_y1, box_x2, box_y2], fill=(0, 0, 0, 133))  # Adjust the transparency as needed
    
    # Blur the transparent rectangle
    blurred_rect = rect_image.filter(ImageFilter.BLUR)
    
    # Paste the blurred transparent rectangle onto the background image
    background_image.paste(blurred_rect, (0, 0), blurred_rect)
    
    
    # Draw the text with black color (shadow) and white color
    for line in lines:
        #shadow_position = (x + shadow_offset[0], y + shadow_offset[1])
        #draw.text(shadow_position, line, fill=shadow_color, font=font)
        draw.text((x, y), line, fill=text_color, font=font)
        y += textsize(line, font=font)[1]  # Move to the next line
    
    draw.text((x, y), author, fill=text_color, font=font)

     # Blur the text overlay
    #blurred_text_overlay = background_image.filter(ImageFilter.BLUR)

     # Paste the blurred text overlay onto the background image
    #background_image.paste(blurred_text_overlay, (0, 0), blurred_text_overlay)


    # File path where you want to save the downloaded image
    number = random_4_digit_number()    
    image_with_text = "image_"+ number +"_text.png"
    # Combine the relative path and file name    
    file_path_text = os.path.join(relative_path, image_with_text)
    
    background_image.save(file_path_text, format="PNG")
    print("Image saved to " + file_path_text)
    


def read_text_from_file(file_path, encodings=['utf-8', 'iso-8859-9', 'latin-1', 'cp1254']):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                quote = file.readline()
                author = file.readline()
            return quote, author
        except UnicodeDecodeError:
            continue
    raise ValueError("Unable to decode the file using any of the specified encodings.")



def add_text_with_shadowBlurred(image_path, quote, author, font_size=30, text_color=(255, 255, 255), shadow_color=(0, 0, 0), shadow_offset=(2, 2), margin=50, max_line_width=500):
    # Open the image
    background_image = Image.open(image_path)
    
    # Create a drawing object
    #draw = ImageDraw.Draw(background_image)
    # Create a blank image with transparent background
    text_overlay = Image.new("RGBA", background_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_overlay)
    
    # Load a font
    font = ImageFont.load_default()  # You can also load a specific font using ImageFont.truetype()
    
    # Calculate text size and position
    #font = ImageFont.truetype("arial.ttf", font_size)
    #font = ImageFont.truetype("pala.ttf", font_size)
    font = ImageFont.truetype("calibri.ttf", font_size)
    #max_text_width = min(max_line_width, image.width - 2 * margin)
    max_text_width = background_image.width - 2 * margin
    
    
    # Wrap the text to fit within the maximum line width
    wrapped_text = textwrap.fill(quote, width=(max_text_width // font_size) * 2.2) #(max_text_width // font_size) * 2)
    
    # Split the wrapped text into multiple lines
    lines = wrapped_text.split('\n')
    
    # Calculate total text height
    total_text_height = sum(textsize(line, font=font)[1] for line in lines)
    
    # Calculate text position
    x = (background_image.width - max_text_width) / 2
    y = (background_image.height - total_text_height) / 7
    
    # Draw the text with black color (shadow) and white color
    for line in lines:
        shadow_position = (x + shadow_offset[0], y + shadow_offset[1])
        draw.text(shadow_position, line, fill=shadow_color, font=font)
        draw.text((x, y), line, fill=text_color, font=font)
        y += textsize(line, font=font)[1]  # Move to the next line
    
    draw.text((x, y), author, fill=text_color, font=font)

    # Blur the text overlay
    blurred_text_overlay = text_overlay.filter(ImageFilter.BLUR)
    

    # Paste the blurred text overlay onto the background image
    #blurred_background = Image.alpha_composite(background_image, blurred_text_overlay)
    # Paste the blurred text overlay onto the background image
    blurred_background = Image.alpha_composite(background_image.convert("RGBA"), blurred_text_overlay.convert("RGBA"))


    
    background_image.save(file_path_text)
    print("Image saved to " + file_path_text)

content_file_path = "content.txt"
quote, author = read_text_from_file(content_file_path)
print(quote)
add_text_with_shadow_box(file_path, quote, author, font_size=88, text_color=(255, 255, 255), shadow_color=(0, 0, 0), shadow_offset=(3, 3), margin=33)
#add_text_with_shadow_box(file_path, quote, author, font_size=88, text_color=(255, 255, 255), shadow_color=(255, 255, 255), shadow_offset=(0, 0), margin=33)
#add_text_with_shadow_box(file_path, quote, author, font_size=88, text_color=(0, 0, 0), shadow_color=(255, 255, 255), shadow_offset=(3, 3), margin=33)
#add_text_with_shadow_box(file_path, quote, author, font_size=88, text_color=(0, 0, 128), shadow_color=(255, 255, 255), shadow_offset=(3, 3), margin=33)
#orange white
add_text_with_shadow_box(file_path, quote, author, font_size=88, text_color=(255, 165, 0), shadow_color=(0, 0, 0), shadow_offset=(3, 3), margin=33)

