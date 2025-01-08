import requests 
import os
from urllib.parse import urlsplit, unquote



def get_extension_file(link):
    decoded_link = unquote(link)
    adress = urlsplit(decoded_link).path
    filename = os.path.split(adress)[-1]
    namefile, formatfile = os.path.splitext(filename)
    return formatfile


def download_images(image_urls, download_folder='images', image_name='nasa_epic'):
    os.makedirs(download_folder, exist_ok=True)

    for number_link, link in enumerate(image_urls):
            response = requests.get(link)
            response.raise_for_status()
            file_extension = get_extension_file(link)
            file_path = os.path.join('images', f'{image_name}{number_link}{file_extension}')
            with open(file_path, 'wb') as file:
                file.write(response.content)
    