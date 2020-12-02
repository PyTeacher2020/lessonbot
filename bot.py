import telebot
import bdmodul
import Buttons

#main variables

TOKEN = "1298948503:AAGO1d4eqOmI8Tvo-VXDkspnpYVCjH792n8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, bdmodul.vk())

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
    bot.send_message(message.chat.id, 'Тыкни на кнопку'+str(message.chat.id),reply_markup=Buttons.start_menu())

@bot.message_handler(content_types= 'text' )
def process_step(message):
    # if message.text=='🔍Найти вакансию':
    #     msg = bot.reply_to(message, 'Введите запрос для поиска вакансии:')
    #     bot.register_next_step_handler(msg, statistics)
    # if message.text=='📊 Статистика':
    #     print('статистика')
    if message.text=='⚙Настройки':
        msg = bot.reply_to(message, 'Советуем оставить настройки "по-умолчанию, если вы не понимаете, какой параметр они регулируют😊',reply_markup=Buttons.settings())
        bot.register_next_step_handler(msg, settings)



@bot.message_handler(content_types= 'text' )
def settings(message):
    if message.text == '💲Расчет зарплаты':
         msg=bot.reply_to(message,'Выберите коэф. расчета ЗП. Описание расчета',reply_markup=Buttons.salary_set('Средняя ЗП по MIN','set1'))
         bot.register_next_step_handler(msg, settings)
    if message.text == '⬅':
        msg=bot.reply_to(message,'Выберите один из пунктов меню, чтобы продолжить',reply_markup=Buttons.start_menu())
        bot.register_next_step_handler(msg, process_step)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global salary_calc
    if call.message:
        if call.data == "set1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите коэф. расчета ЗП. Описание расчета",reply_markup=Buttons.salary_set('Средняя ЗП: по MAX','set2'))
            salary_calc='max'

        if call.data == "set2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите коэф. расчета ЗП. Описание расчета",
                                  reply_markup=Buttons.salary_set('Средняя ЗП: по MIN','set1'))
            salary_calc = 'min'
    print(salary_calc)

bot.polling()
