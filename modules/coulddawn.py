'''
Модуль для высчитывания времени колудауна
'''

async def get_coulddawn_text(coulddawn: int):
    '''Текст об окончании кулдауна'''
    if coulddawn > 59:
        result = '{} мин.'.format(int(coulddawn // 60))
    else:
        result = '{} сек.'.format(int(coulddawn))
    return result