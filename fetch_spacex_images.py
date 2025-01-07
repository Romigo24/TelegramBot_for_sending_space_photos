import requests
import argparse
from modules import download_images


def get_latest_launch_id():
    response = requests.get("https://api.spacexdata.com/v5/launches/latest")
    response.status_code
    return response.json()['id']

def fetch_spacex_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.status_code
    launch = response.json()
    image_urls = launch.get("links", {}).get("flickr", {}).get("original", [])
    download_images(image_urls, download_folder='images', image_name='spacex')

def main():
    parser = argparse.ArgumentParser(description='Скачать фотографии SpaceX по ID запуска')
    parser.add_argument('-launch_id', help='ID запуска SpaceX')
    args = parser.parse_args()
    launch_id = args.launch_id or get_latest_launch_id()
    if launch_id:
        fetch_spacex_launch(launch_id)


if __name__ == '__main__':
    main()