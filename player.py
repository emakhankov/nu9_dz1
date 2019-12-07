from card import *


class Player:

    def __init__(self, name):
        self.name = name
        self.card = Card()

    def card_str(self):

        return f'Карточка игрока: {self.name}\n{self.card}'

    def print_card(self):

        print(self.card_str())

    def ask_for_barrel(self, barrel, delegate=None):

        self.card.accept_barrel(barrel.get_num())
        return True

    def is_winner(self):

        return not self.card.amount_num()

    def __str__(self):

        self.card_str()

    def __eq__(self, other):

        if type(self) == type(other):
            return self.name == other.name
        return False

    def __ne__(self, other):

        return not __eq__(other)


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
