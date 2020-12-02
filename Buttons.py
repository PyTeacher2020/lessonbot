from telebot import types

def start_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add('🔍Найти вакансию')
    markup.add('📊 Статистика')
    markup.add('⚙Настройки')
    return markup


def salary_set(butt_text,butt_answ):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text=butt_text, callback_data=butt_answ)
    markup.add(button1)
    return markup


def settings():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('💲Расчет зарплаты')
    markup.add('⬅')
    # добавить новые кнопки
    return markup
