from PIL import Image
import pywhatkit as kt
import requests

ALBUM_IMG_NAME = "albumImage.png"




image_url = "https://i.scdn.co/image/ab67616d0000b27333b8541201f1ef38941024be"
response = requests.get(image_url)

if response.status_code == 200:
    with open(ALBUM_IMG_NAME, "wb") as f:
        f.write(response.content)
else:
    print("Failed to download the image")


source_path = ALBUM_IMG_NAME
target_path = 'albumASCII.text'

imagepath = './albumImage.png'
# image = Image.open('spotify-player/' + ALBUM_IMG_NAME)
image = Image.open('./albumImage.png')


# Resize the image for better ASCII art representation
image = image.resize((100, 200))


kt.image_to_ascii_art(image, target_path)
