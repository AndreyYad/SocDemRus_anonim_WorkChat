'''
Модуль для получения конфиг-данных
'''

from json import load

with open('config.json') as file:
    config = load(file)

TOKEN = config.get('token')
CHAT_FROM = config.get('chat_from')
CHAT_TO = config.get('chat_to')
COULDDAWN = config.get('coulddawn')