from UniformDistribution import uniform_distribution

import numpy as np


class NormalDistribution:
    """Generates normal distribution from the uniform distribution using Box-Muller tranform"""

    def __init__(self, mu, sigma):
        """Initialize coefficients"""
        self.unif_dist1 = uniform_distribution.UniformDistribution(0, 1)
        self.unif_dist2 = uniform_distribution.UniformDistribution(0, 1)

        self.sigma = sigma
        self.mu = mu

    def getData(self, amount):
        """Return distribution"""
        data1 = self.unif_dist1.getData(amount)
        data2 = self.unif_dist2.getData(amount)

        dist = []
        j1, j2 = 0, 0
        for i in range(amount):
            # Standard normal pair
            z0 = np.sqrt(-2 * np.log(data1[j1])) * np.cos(2 * np.pi * data2[j2])
            z1 = np.sqrt(-2 * np.log(data1[j1])) * np.sin(2 * np.pi * data2[j2])

            # Scaling
            z0 = z0 * self.sigma + self.mu
            z1 = z1 * self.sigma + self.mu

            if j1 == amount:
                j1 = 0

            if j2 == amount:
                j2 = 0

            dist.append(z0)
            dist.append(z1)

            j1 += 1
            j2 += 1

        return dist
