import barrel as bl
import random


class Bag:

    def __init__(self):

        self.barrels = {bl.Barrel(num) for num in range(1, 91)}

    def get_barrel(self):
        if self.barrels:
            barrel = random.sample(self.barrels, 1)[0]
            self.barrels.remove(barrel)
            return barrel
        else:
            return None

    def get_count(self):

        return len(self.barrels)

    def __len__(self):

        return len(self.barrels)

    def __getitem__(self, item):

        return sorted(list(self.barrels))[item]

    def __eq__(self, other):

        if isinstance(other, Bag):
            return {barrel.get_num() for barrel in self} == {barrel.get_num() for barrel in other}
        return False

    def __ne__(self, other):

        return not self.__eq__(other)

    def __str__(self):

        return ' '.join([str(b) for b in self.barrels]) if self.barrels else 'Пустой бочонок'

    def __contains__(self, item):

        return item.get_num() in {barrel.get_num() for barrel in self}
