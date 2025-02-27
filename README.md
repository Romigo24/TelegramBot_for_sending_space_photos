# Автоматическая публикация фотографий в Telegram-канал

Этот скрипт предназначен для автоматической публикации фотографий из указанной директории в Telegram-каал с заданным интервалом.

### Как установить
Установите [Python](https://www.python.org/downloads/) версии 3.10.
Клонируйте репозиторий себе на компьютер командой:
```
git clone https://github.com/Romigo24/TelegramBot_for_sending_space_photos
```
Но для корректной работы приложения вам потребуется установить следующие переменные окружения:

- **`TG_TOKEN`** - Токен ключ для вашего Telegram-бота, который можно получить у [BotFather](https://t.me/botfather) ([регистрация бота](https://way23.ru/регистрация-бота-в-telegram.html))
- **`TG_CHANNEL_ID`** - ID вашего [Telegram-канала](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/), куда будут отправляться фотографии. Убедитесь, что бот является администратором канала.
- **`INTERVAL`** - Интервал между публикациями (по умолчанию 4 часа).

Эти переменные нужно внести в файл `.env` в корневой директории проекта.
Создайте виртуальное окружение в корневом каталоге командой:
```
python -m venv env
```
Активируйте виртуальное окружение командой:
```
source env/bin/activate
```
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей командой:
```
pip install -r requirements.txt
```
Затем можем запускать скрипт через IDE или через терминал командой с указанием директории с фотографиями и свои интервалом, если нужно постить фотографии чаще или реже:
```
python telegram_bot.py images 2
```
Готово, ваши фотографии будут публиковаться каждые 2 часа.

### Как использовать скрипты для скачивания фотографий с NASA и SpaceX

Для скачивания фотографий с сайта NASA вам потребуется [API_KEY_NASA](https://api.nasa.gov), добавьте его в файл `.env`.
Запускайте скрипт для скачивания APOD фотографий из терминала командой с указанием количества нужных вам фотографий:
```
python fetch_nasa_apod_images.py 5
```
И так же для скачивания EPIC фотографий:
```
python fetch_nasa_epic_images.py 5
```

Для скачивания фотографий с сайта SpaceX вам потребуется только запустить скрипт командой:
```
python fetch_spacex_images.py
```

Скрипт сам найдет фотографии последнего запуска, но бывает такое что фотографии при запуске не делали, в таком случае вам потребуется ввести самостоятельно ID запуска, вот ID запуска `5eb87d47ffd86e000604b38a`, на котором точно делали фотографии, и команда:
```
python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```
