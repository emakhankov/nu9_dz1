import player as pl
import bag as bg
import random


def delegate_ask(player):

    print(player.name)
    inp = input('Принять значение (Д(а)/Н(ет)')
    return 'д' in inp.lower() or 'y' in inp.lower()


def game(amount_player_human, amount_player_computer):

    print('Начинаем игру')

    list_players = []
    for n_player in range(amount_player_human):
        player = pl.HumanPlayer(f'{n_player+1}')
        list_players.append(player)

    for n_player in range(amount_player_computer):
        player = pl.ComputerPlayer(f'{n_player+1}')
        list_players.append(player)

    random.shuffle(list_players)

    print()
    print('Внимание!!! Порядок ходов игроков задается сейчас в произвольном порядке')
    print()
    print('Игроки и их карточки:')
    for player in list_players:
        player.print_card()
        print()

    bag = bg.Bag()

    print()
    print('*** ПОЕХАЛИ ***')
    print()

    while True:

        barrel = bag.get_barrel()
        if barrel is None:
            print('Бочонков больше нет. Игра окончена')
            return

        print(f'Новый бочонок: {barrel.get_num()} (осталось {bag.get_count()})')
        for player in list_players:
            player.print_card()
            print()

        for player in list_players:
            ret = player.ask_for_barrel(barrel, delegate_ask)
            if not ret:
                print(f'{player.name} - ошибка. Вы проиграли Игра Окончена')
                return
            if player.is_winner():
                print(f'{player.name} - Вы выиграли')
                return

        print()
        print('*** следующий раунд ***')
        print()







