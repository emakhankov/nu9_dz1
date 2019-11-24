from card import *


class Player:

    def __init__(self, name):
        self.name = name
        self.card = Card()

    def print_card(self):
        print('Карточка игрока:', self.name)
        self.card.print_card()

    def ask_for_barrel(self, barrel, delegate=None):

        self.card.accept_barrel(barrel.get_num())
        return True

    def is_winner(self):

        return not self.card.amount_num()


class HumanPlayer(Player):

    def __init__(self, name):

        super().__init__(f'Человек {name}')

    def ask_for_barrel(self, barrel, delegate=None):

        if delegate is None:
            otv = True
        else:
            otv = delegate(self)

        can_acc = self.card.can_accept_barrel(barrel.get_num())
        if otv and can_acc:
            return super().ask_for_barrel(barrel, None)
        elif otv and not can_acc:
            return False
        elif not otv and can_acc:
            return False
        else:
            return True


class ComputerPlayer(Player):

    def __init__(self, name):

        super().__init__(f'Компьютер {name}')


    def ask_for_barrel(self, barrel, delegate):

        return super().ask_for_barrel(barrel)
