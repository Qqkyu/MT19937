from UniformDistribution import uniform_distribution

import numpy as np


class PoissonDistribution:
    """Generator implementing Poisson distribution using uniform distribution"""

    def __init__(self, lmbd, amount):
        """Initialize coefficients"""
        self.unif_dist = uniform_distribution.UniformDistribution(0, 1).getData(amount)

        self.amount = amount
        self.lmbd = lmbd

        self.L = np.exp(-self.lmbd)

    def getData(self):
        """Return distribution"""
        dist = []
        j = 0
        for i in range(self.amount):
            a, b = 0, 1
            while b > self.L:
                a += 1
                b *= self.unif_dist[j]
                j += 1
                if j == self.amount:
                    j = 0

            dist.append(a - 1)
        return dist
