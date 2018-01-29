# NescaTelegramBot
#### NescaTelegramBot - скрипт для автоматического постинга результатов Nesca в Telegram канал. 

# Установка

#### Первым делом устанавливаем все необходимые либы:

1. pip install python-telegram-bot
2. pip install selenium
3. pip install requests
4. pip install codecs
5. pip install bs4

#### Получаем в телеграме токен бота (@BotFather), выдаем ему админ права в канале

#### Правим файл NescaTelegramBot.py

1. Скачиваем драйвер: 
```
github.com/mozilla/geckodriver/releases
```
2. Меняем путь к драйверу:
```
DRIVER = 'D:\Python'
```
3. Меняем BOTTOKEN на свой (который получили у BotFather):
```
bot = telegram.Bot('BOTTOKEN')
```
4. Меняем канал на свой: 
```
channel = '@CHANNELNAME
```
# Запуск

#### Перед запуском рекомендуется дождаться файлов с результатами от Nesca, далее софт можно оставить работать вместе с неской, каждый раз как Nesca находит что-то новое, скрипт запостит ip и скрин в telegram.

1. Запускаем файл NescaTelegramBot.py
2. Вводим расположение файла с результатами нески (на пример: D:\Results\other.html)
3. Для удобства можно кинуть скрипт прямо в папку с результатами и ввести просто: "other.html"


