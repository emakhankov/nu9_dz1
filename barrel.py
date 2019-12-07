
class Barrel:

    def __init__(self, num):

        self.num = num

    def __hash__(self):

        return self.num

    def get_num(self):

        return self.num

    def __str__(self):

        return str(self.num)

    def __eq__(self, other):

        if other is isinstance(other, Barrel):
            return self.get_num() == other.get_num()
        return False

    def __ne__(self, other):

        return not self.__ne__(other)

    def __lt__(self, other):

        return self.get_num() < other.get_num()