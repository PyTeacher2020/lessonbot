from telebot import types


def statistics():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add('📊 Статистика')
    #print('статистика')
    return markup