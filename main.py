from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions
from aiogram.types import Message

from asyncio import new_event_loop

from os import mkdir

from modules.config import TOKEN, CHAT_TO, COULDDAWN
from modules.bot_cmds import *
from modules.sql_cmds import *
from modules.coulddawn import *
from modules.messages import MESSAGES

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print('Бот запущен!')

@dp.message_handler(commands = ['start'])
async def start_func(msg: Message):
    if msg.chat.type == 'private':
        await send_msg(msg.from_user.id, MESSAGES['start'])

@dp.message_handler()
async def say_func(msg: Message):
    user_id = msg.from_user.id
    msg_time = msg.date.timestamp()
    if msg.chat.type == 'private':
        try:
            if await check_user_in_chat(user_id):
                cd = await get_end_cd(user_id) - msg_time
                if cd <= 0:
                    await set_end_cd(user_id, msg_time + COULDDAWN)
                    await send_msg(CHAT_TO, msg.text)
                    await send_msg(user_id, 'Сообщение отправлено в "{}"!'.format(await get_chat_name('to')))
                else:
                    await send_msg(user_id, 'Ещё один запрос сможете отправить только через {}'.format(await get_coulddawn_text(cd)))
            else:
                await send_msg(user_id, 'Вы не состоите в "{}"!'.format(await get_chat_name('from')))
        except exceptions.ChatNotFound:
            print('Не найден один или оба чата!')

def getComissionChatId(msg:Message):
    return msg.chat.id
    
if __name__ == '__main__':
    try:
        mkdir('database')
    except FileExistsError:
        pass
    loop = new_event_loop()
    loop.run_until_complete(born_of_db())
    executor.start_polling(dp)