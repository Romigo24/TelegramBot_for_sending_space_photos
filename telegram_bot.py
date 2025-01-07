import telegram
import os
from dotenv import load_dotenv


load_dotenv()
BOT = telegram.Bot(token=os.environ['TG_TOKEN'])
CHANNEL_ID = os.environ['TG_CHANNEL_ID']


def main():
    BOT.send_photo(chat_id=CHANNEL_ID, photo=open('images/nasa_apod6.jpg', 'rb'))

if __name__ == '__main__':
    main()