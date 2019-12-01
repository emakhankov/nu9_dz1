from game import *
from menu import *


def go_to_game():

    ans_human = menu('Введите кол-во игроков (людей)', ['1. 1-игрок', '2. 2-игрока', '0. Без людей'], ['1', '2', '0'])
    ans_computer = menu('Введите кол-во игроков (компьютеров)', ['1. 1-игрок', '2. 2-игрока', '0. Без компьютеров'],
                        ['1', '2', '0'])
    if int(ans_human) + int(ans_computer) == 0:
        print('Нужен хотя-бы один игрок, хоть сам с собой')
        return
    game(int(ans_human), int(ans_computer))


while True:

    print('***', "ИГРА ЛОТО", '***')
    ans = menu('ГЛАВНОЕ МЕНЮ', ['1. Начать игру', '0. Выход'], ['1', '0'])
    if ans == '1':
        go_to_game()
    elif ans == '0':
        break
