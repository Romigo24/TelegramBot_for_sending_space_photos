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
    if not os.path.exists(download_folder):
        os.mkdir(download_folder)

    for number_link, link in enumerate(image_urls):
            response = requests.get(link)
            response.status_code
            file_extension = get_extension_file(link)
            file_path = os.path.join('images', f'{image_name}{number_link}{file_extension}')
            with open(file_path, 'wb') as file:
                file.write(response.content)
    
