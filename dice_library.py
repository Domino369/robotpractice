from dice import Dice

class DiceLibrary(object):
    """Dice library for rolling random numbers"""
    def __init__(self):
        self._die = Dice()
        self._result = ''

    def roll(self, die_size):
        """Rolls die"""

        die_size = int(die_size)
        self._result = self._die.d(die_size)

    def result_should_be(self, die_size):
        """Verifies result"""

        die_size = int(die_size)
        if self._result not in range(die_size+1):
            raise AssertionError('%s not in 1 ~ %s' % (self._result, die_size))

    def should_cause_error(self, die_size):
        """Verifies a result gives an exception"""

        die_size = int(die_size)
        try:
            self._die.d(die_size)
        except Error, err:
           return str(err)
