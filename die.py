import random

class die:
    def __init__(self):
        pass

    def roll(self):
        num = random.randint(1,6)
        print(num)
        return num



d1 = die()
d2 = die()