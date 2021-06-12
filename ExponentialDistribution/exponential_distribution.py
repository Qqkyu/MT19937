from UniformDistribution import uniform_distribution

import numpy as np


class ExponentialDistribution:
    """Generates exponential distribution from the uniform distribution"""

    def __init__(self, lmbd):
        """Initialize coefficients"""
        self.unif_dist = uniform_distribution.UniformDistribution(0, 1)

        self.lmbd = lmbd

    def getData(self, amount):
        """Return distribution"""
        data = self.unif_dist.getData(amount)

        dist = []
        j = 0
        for i in range(amount):
            dist.append(-(1 / self.lmbd) * (np.log(1 - data[j])))
            j += 1
            if j == amount:
                j = 0

        return dist
