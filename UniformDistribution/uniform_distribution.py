from MersenneTwister import MT19937

import random
import sys


class UniformDistribution:
    """Generator implementing uniform distribution using MT19937"""

    def __init__(self, low, high):
        """Initialize MT19937 and coefficients"""
        seed_val = random.randrange(sys.maxsize)
        self.MT19937 = MT19937.MT19937(seed_val)

        self.low = low
        self.high = high

        self.range = self.high - self.low

        self.RAND_MAX = self.MT19937.RAND_MAX

    def extractNumber(self):
        number = self.MT19937.extractNumber() / (1.0 + self.RAND_MAX)
        scaled_number = (number * self.range) + self.low
        return scaled_number

    def getData(self, amount):
        """Create array of <amount> uniformly distributed numbers"""
        data = []
        for i in range(0, amount):
            data.append(self.extractNumber())
        return data
