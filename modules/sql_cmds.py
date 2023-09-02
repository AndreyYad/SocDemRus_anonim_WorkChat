'''Методы связаные с работой с базами данных'''

from aiosqlite import connect

from asyncio import run

async def born_of_db():
    '''Создание таблиц'''
    async with connect('database/msg_time.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("CREATE TABLE IF NOT EXISTS msg (user_id int PRIMARY KEY, time_end_cd int)")
        await conn.commit()

async def set_end_cd(user_id: int, time_end_cd: int):
    '''Сохранение времени окончания коулдауна'''
    async with connect('database/msg_time.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("INSERT OR IGNORE INTO msg (user_id) VALUES (?)", (user_id,))
        await cur.execute("UPDATE msg SET time_end_cd = ? WHERE user_id = ?", (time_end_cd, user_id))
        await conn.commit()

async def get_end_cd(user_id: int):
    '''Получение времени окончания коулдауна'''
    async with connect('database/msg_time.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("SELECT time_end_cd FROM msg WHERE user_id = ?", (user_id,))
        try:
            result = (await cur.fetchall())[0][0]
        except IndexError:
            result = 0
    return result

if __name__ == '__main__':
    print(run(born_of_db()))