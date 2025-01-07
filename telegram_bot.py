import telegram
import os
from dotenv import load_dotenv


load_dotenv()
BOT = telegram.Bot(token=os.environ['TG_TOKEN'])
CHANNEL_ID = os.environ['TG_CHANNEL_ID']


def main():
    message = 'test message'
    BOT.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == '__main__':
    main()