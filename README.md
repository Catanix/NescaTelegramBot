# NescaTelegramBot
#### NescaTelegramBot - скрипт для автоматического постинга результатов Nesca в Telegram канал.

![1](https://user-images.githubusercontent.com/35846376/35504570-9c039c68-050d-11e8-908f-f62e68d981d7.png)

![1](https://user-images.githubusercontent.com/35846376/35504570-9c039c68-050d-11e8-908f-f62e68d981d7.png)

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
2. Добавляем папку с драйвером в PATH (в win желательно вынести запись в первые ряды):
```
'D:\Python\Driver\Geckodriver'
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
