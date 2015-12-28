import random

class Dice(object):
    """Dice object for rolling random numbers"""

    def d(self, die_size):
        """Rolls a dx die"""

        return random.randint(0, die_size)

if __name__ == '__main__':
    dice = Dice()
