import random
from string import ascii_uppercase, digits
class Robot:
    def __init__(self):
        random.seed()
        upper = random.choices(ascii_uppercase, k=2)
        digs = random.choices(digits, k=3)
        self.name = "".join(upper + digs)
    def reset(self):
        self.__init__() 