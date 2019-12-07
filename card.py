import random


class Card:

    def __init__(self):

        random_list = list(range(1, 91))
        random.shuffle(random_list)
        self.nums = [list(sorted(random_list[i*5:i*5+5])) for i in range(3)]
        self.gaps = []
        for i in range(3):
            gaps = [i for i in range(9)]
            random.shuffle(gaps)
            self.gaps.append(gaps[0:4])

        lines = []
        for i in range(3):
            line = []
            n = 0
            for j in range(9):
                if j in self.gaps[i]:
                    line.append(None)
                else:
                    line.append(self.nums[i][n])
                    n += 1
            lines.append(line)
        self.lines = lines

    def card_str(self):

        s = []
        for i in range(3):
            s_line = []
            for j in range(9):
                if self.lines[i][j] is None:
                    s_line.append(' ' * 4)
                else:
                    s_line.append(f' {self.lines[i][j]:2} ')
            s.append(''.join(s_line))
        return f'\n'.join(s)

    def print_card(self):

        print(self.card_str())
        print()

    def can_accept_barrel(self, num):

        for i in range(3):
            if num in self.lines[i]:
                return True
        return False

    def accept_barrel(self, num):

        for i in range(3):
            if num in self.lines[i]:
                ind = self.lines[i].index(num)
                self.lines[i][ind] = '--'
                return True
        return False

    def amount_num(self):

        amount = 0
        for i in range(3):
            for j in range(9):
                if isinstance(self.lines[i][j], int):
                    amount += 1
        return amount

    def __str__(self):

        return self.card_str()

    def __len__(self):

        return len(self.amount_num())

    def __iter__(self):

        for i in range(3):
            for j in range(9):
                if isinstance(self.lines[i][j], int):
                    yield int(self.lines[i][j])
        raise IndexError

    def __eq__(self, other):

        if isinstance(other, Card):
            return {digit for digit in self} == {digit for digit in other}
        return False

    def __ne__(self, other):

        return not __eq__(other)
