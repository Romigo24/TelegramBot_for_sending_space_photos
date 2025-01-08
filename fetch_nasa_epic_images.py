import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from modules import download_images
import argparse
from urllib.parse import urlencode

api_key_nasa = os.environ['API_KEY_NASA']

def fetch_images_nasa_epic(api_key_nasa, count):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key_nasa
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    image_urls = []
    for image in range(min(len(images), count)):
        image_data = images[image]
        image_date = image_data['date'].split(' ')[0]
        date = datetime.strptime(image_date, '%Y-%m-%d')
        image_name = image_data['image']
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{date.strftime('%Y/%m/%d')}/png/{image_name}.png?{urlencode(params)}"   #api_key={api_key_nasa}"
        image_urls.append(image_url)
        download_images(image_urls, download_folder='images', image_name='nasa_epic')

if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Скрипт для загрузки EPIC фотографий с сайта NASA')
    parser.add_argument('--count', type=int, default=10, help='Количество фотографий для загрузки')
    args = parser.parse_args()
    fetch_images_nasa_epic(api_key_nasa, args.count)