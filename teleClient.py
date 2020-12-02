import configparser

from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetInlineBotResultsRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
destination=config['Telegram']['test_bot']


def connect(username,api_id,api_hash):
    client = TelegramClient(username, api_id, api_hash)
    client.start()
    return client


def send_message(client,destination,message):
    entity=client.get_entity(destination)
    mess=client.send_message(entity=entity,message=message)
    return mess


def inline_butt(c,destination,username):

    bot_results = c(GetInlineBotResultsRequest(destination, username, 'call', ''))



c=connect(username,api_id,api_hash)
send_message(c,destination,'/start')
send_message(c,destination,'⚙Настройки')
send_message(c,destination,'💲Расчет зарплаты')
inline_butt(c,destination,username)
# print(send_message(c,'lessongeek_bot','/start'))
# #
# for message in c.iter_messages('botforlesson'):
#     print(message)

# @c.on(events.NewMessage(chats=('chat_name')))
# async def normal_handler(event):
# #    print(event.message)
#     print(event.message.to_dict()['message'])
#
#
# c.loop.run_until_disconnected()
print(2)
