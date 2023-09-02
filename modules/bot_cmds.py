'''Модуль с командами для бота'''

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from typing import Callable

from asyncio import run

try:
    from modules.config import TOKEN, CHAT_FROM, CHAT_TO
except ModuleNotFoundError:
    from config import TOKEN, CHAT_FROM, CHAT_TO

def bot_setup(func: Callable):
    '''
    Обёртка с подключением и отключением сесии бота
    '''
    async def wrapper(*args, **kwargs):
        bot = Bot(token=TOKEN)
        dp = Dispatcher(bot)
        res = await func(*args, **kwargs, dp=dp)
        session = await bot.get_session()
        await session.close()
        return res
    return wrapper

@bot_setup
async def send_msg(chat_id: int, text: str, web_prew: bool=False, dp: Dispatcher | None=None, **kwargs):
    '''Отправка сообщения'''
    await dp.bot.send_message(chat_id, text, parse_mode='html', disable_web_page_preview=not web_prew, **kwargs)

@bot_setup
async def check_user_in_chat(user_id: int, dp: Dispatcher | None=None):
    '''Проверка на членство в чате'''
    return (await dp.bot.get_chat_member(CHAT_FROM, user_id))['status'] != 'left'

@bot_setup
async def get_chat_name(which_chat: str, dp: Dispatcher | None=None):
    '''Проверка на членство в чате'''
    chat_id = {'from' : CHAT_FROM, 'to' : CHAT_TO}[which_chat]
    return (await dp.bot.get_chat(chat_id))['title']

if __name__ == '__main__':
    # print(run(get_chat_from_name()))
    pass