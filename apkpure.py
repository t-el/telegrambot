import os
import telebot
import lxml
from lxml import html
from telebot import types
import requests
import selenium
from selenium import webdriver


headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

TOKEN = "1960744179:AAHNB1dDaBdOiXco3aUhz-eKNDADBtHzCN4"

bot = telebot.TeleBot(TOKEN)
#########################################################################################
@bot.message_handler(commands=["start"])
def start_command(message):
    msg = " Please welcome "+message.chat.username+"\n This bot is created by @TahaElkarroumy\n"
    msg+="To enable you to download android apps using the legendary Telegram \nI hope you enjoy\n"
    msg+="use /search to search apps and games"
    bot.send_message(message.chat.id,msg)


@bot.message_handler(commands=["search"])
def search(message):
    msg = "Type the name of the application or game  you want"
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,msg)   


      
@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_search_query(message):
    msg = "looking for <b> "+message.text+"</b>"
    res = requests.get("https://m.apkpure.com/search?q="+message.text,headers=headers)
    xml = html.fromstring(res.content)
    xp = xml.xpath("//*[@id='search-res']/li")
    msg+="\n<b>"+str(len(xp))+"</b> app being founded"
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,msg,parse_mode='html', disable_web_page_preview=True)
    
    for i, x in enumerate(xp):
            try:
                app_img = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[1]/img/@src")
                app_name = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[2]/p[1]/text()") 
                app_rate = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[2]/div/span[2]/text()")
                app_dev = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[2]/p[2]/text()")
                app_link = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/@href")
                msg= "Name : <b><i>"+app_name[0]+"</i></b>\n"+"Rate : <b>"+app_rate[0]+"</b>\nDevelopper : <b>"+app_dev[0]+"</b>"
                msg+="\nDownload link : <b>https://m.apkpure.com"+app_link[0]+"</b>"
                bot.send_message(message.chat.id,msg,parse_mode='html', disable_web_page_preview=True)   
            except Exception as e:
                continue


#for i, x in enumerate(xp):
    #app_img = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[1]/img/@src")
    #app_name = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[2]/p[1]/text()") 
    #app_rate = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[2]/div/span[2]/text()")
    #app_dev = xml.xpath("//*[@id='search-res']/li["+str(i+1)+"]/dl/a/div[2]/p[2]/text()")

bot.polling()    