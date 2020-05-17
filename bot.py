import telebot
import bdmodul

#main variables

TOKEN = "1298948503:AAGO1d4eqOmI8Tvo-VXDkspnpYVCjH792n8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я твой маленький помощник')

@bot.message_handler(commands=['help'])
def process_help_command(message):
    bot.send_message(message.chat.id, 'Я знаю следующие команды:\n /Show \n /Edit \n /Add \n /Delete \n')
    
@bot.message_handler(commands=['Show'])
def process_show_command(message):
    with open('books.csv') as database:
        for i in database:
            bot.send_message(message.chat.id,i)

@bot.message_handler(commands=['button'])
def activate_butt(message):
    bot.send_message(message.chat.id, 'Тыкни на кнопку',reply_markup=markup)

    
bot.polling()
