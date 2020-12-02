import pytest
import configparser
import teleClient

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
test_bot=config['Telegram']['test_bot']

@pytest.fixture(scope='session')
def initial():
    client = teleClient.connect(username, api_id, api_hash)
    return client

# def test_connection():
#     assert teleClient.connect(username,api_id,api_hash).is_connected()== True


def test_connection(initial):
    assert  initial.is_connected()== True


def test_send_message(initial):
    assert teleClient.send_message(initial,test_bot,'/start')==True



