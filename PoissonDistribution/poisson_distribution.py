from UniformDistribution import uniform_distribution

import numpy as np


class PoissonDistribution:
    """Generator implementing Poisson distribution using uniform distribution"""

    def __init__(self, k, lmbd):
        """Initialize coefficients"""
        self.unif_dist = uniform_distribution.UniformDistribution(0, 1).getData(k)

        self.k = k
        self.lmbd = lmbd

        self.L = np.exp(-self.lmbd)

    def getData(self):
        """Return distribution"""
        dist = []
        j = 0
        for i in range(1, self.k - 1):
            a, b = 0, 1
            while b > self.L:
                a += 1
                b *= self.unif_dist[j]
                j += 1
                if j == self.k:
                    j = 0

            dist.append(a - 1)
        return dist
