from selenium import webdriver
from bs4 import BeautifulSoup
import telegram #python-telegram-bot
import datetime
import requests
import codecs
import time
import os

def parse(path):
    try:
        adress=[]
        source = codecs.open(path, 'r', 'utf-8')
        Soup = BeautifulSoup(source.read(), "html.parser")
        ips = Soup.findAll("span", {"id": "hostSpan"})
        for ip in ips:
            adress.append(ip.getText())
        return(adress)
    except:
        pass

def screenshot(ip):
    try:
        # Download driver here: https://github.com/mozilla/geckodriver/releases
        driver = webdriver.Firefox()
        driver.get('http://'+ip)
        screenshot = driver.save_screenshot('web.png')
        driver.quit()
    except:
        pass

def Start():
    bot = telegram.Bot('BOTTOKEN') # Bot token (@BotFather)
    channel = '@CHANNEL' # Telegram channel name (@ExampleChannel)
    ip_list = []
    print('Nesca output files path:')
    path = input()
    while True:
        try:
            adress=parse(path)
            for ip in adress:
                 if ip not in ip_list:
                     now = str(datetime.date.today())
                     ip_list.append(ip)
                     screenshot(ip)
                     print(now)
                     bot.send_message(chat_id=channel, text="Date: "+now+"\nIp: http://"+ip)
                     bot.send_photo(chat_id=channel, caption="http://"+ip, photo=open('web.png', 'rb'))
                     print('Post created: '+'http://'+ip)
                     os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'web.png'))
            time.sleep(10)
        except:
            pass

Start()

#WEBSEEKERMOODUCK
