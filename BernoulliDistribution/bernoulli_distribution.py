import MT19937

import random
import sys


class BernoulliDistribution:
    """Generator implementing Bernoulli distribution using MT19937"""

    def __init__(self, p):
        """Initialize MT19937 and coefficients"""
        seed_val = random.randrange(sys.maxsize)
        self.MT19937 = MT19937.MT19937(seed_val)

        self.p = p

        self.RAND_MAX = self.MT19937.RAND_MAX

    def extractNumber(self):
        number = self.MT19937.randomUnif()
        return number > self.p

    def getData(self, amount):
        """Return number of successful trials"""
        successful_trials = 0
        for i in range(0, amount):
            successful_trials += self.extractNumber()
        return successful_trials
