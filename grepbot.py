import os
import telebot
import lxml
from lxml import html
from telebot import types
import requests

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

TOKEN = "1974546758:AAFR2tv1s9KTrIoYwi75gfPZMibabG0F3Hk"

bot = telebot.TeleBot(TOKEN)
#########################################################################################
@bot.message_handler(commands=["start"])
def start_command(message):
    msg = " Please welcome "+message.chat.username+"\n This bot is created by @TahaElkarroumy\n"
    msg+="To enable you search for codes in githup  using the legendary Telegram \nI hope you enjoy\n"
    msg+="use /search"
    bot.send_message(message.chat.id,msg)


@bot.message_handler(commands=["search"])
def search(message):
    msg = "Type a keyword "
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,msg)   

@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_search_query(message):
    msg = "looking for <b> "+message.text+"</b>"
    res = requests.get("https://grep.app/search?q="+message.text,headers=headers)
    xml = html.fromstring(res.content)
    xp = xml.xpath("")


bot.polling()