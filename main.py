from game import *
from menu import *


def go_to_game():

    ans_human = menu('Введите кол-во игроков (людей)', ['1. 1-игрок', '2. 2-игрока'], ['1', '2'])
    ans_computer = menu('Введите кол-во игроков (компьютеров)', ['1. 1-игрок', '2. 2-игрока'], ['1', '2'])
    game(int(ans_human), int(ans_computer))


while True:

    print('***', "ИГРА ЛОТО", '***')
    ans = menu('ГЛАВНОЕ МЕНЮ', ['1. Начать игру', '0. Выход'], ['1', '0'])
    if ans == '1':
        go_to_game()
    elif ans == '0':
        break
