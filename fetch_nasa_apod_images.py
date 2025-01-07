import requests
import os
from dotenv import load_dotenv
from modules import download_images


load_dotenv()
api_key_nasa = os.environ['API_KEY_NASA']

def fetch_images_nasa_apod(api_key_nasa, count):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key_nasa,
        'count': count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    image_urls = [url['url'] for url in response.json()]
    download_images(image_urls, download_folder='images', image_name='nasa_apod')

if __name__ == '__main__':
    fetch_images_nasa_apod(api_key_nasa, count=30)