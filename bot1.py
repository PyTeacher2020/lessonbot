import telebot
import button
import datetime
from test import *

now = datetime.datetime.now()
TOKEN = "1452055338:AAEnZSyZqQuAT2ekDbvPx-DyO3BYKiJSFLw"
bot = telebot.TeleBot(TOKEN)
#.............
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id,'Привет :)',reply_markup=button.statistics())
#сообщение для кнопки "статистика"
mess='\nНа '+ now.strftime("%d-%m-%Y %H:%M") +  '\nInstagram: ' + inst()+'\nFacebook: '+ fcbook()

@bot.message_handler(content_types= 'text' )
def process_step(message):
    if message.text=='📊 Статистика':
        msg = bot.reply_to(message, mess)

bot.polling()