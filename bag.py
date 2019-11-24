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



