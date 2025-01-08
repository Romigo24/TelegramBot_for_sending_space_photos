import telegram
import os
from dotenv import load_dotenv
import random 
import time
import argparse


BOT = telegram.Bot(token=os.environ['TG_TOKEN'])
CHANNEL_ID = os.environ['TG_CHANNEL_ID']

def publish_photos(directory, interval):
    images = os.listdir(directory)
    
    while True:
        random.shuffle(images)

        for image in images:
            image_path = os.path.join(directory, image)
            with open(image_path, 'rb') as image:
                BOT.send_photo(chat_id=CHANNEL_ID, photo=image)
                time.sleep(interval * 3600)        


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Скрипт для автоматической публикации в Telegram-канал.')
    parser.add_argument('directory', type=str, help='Путь к директории с изображениями')
    parser.add_argument('--interval', type=int, default=os.getenv('INTERVAL', 4), help='Интервал между публикациями в часах')
    args = parser.parse_args()
    publish_photos(args.directory, args.interval)
    