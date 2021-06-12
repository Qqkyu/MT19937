from BernoulliDistribution import bernoulli_distribution

import math


def binom(n, k):
    """Calculates binomial coefficient"""
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))


class BinomialDistribution:
    """Generator implementing binomial distribution using Bernoulli distribution"""

    def __init__(self, p, n):
        """Initialize coefficients"""
        self.bern = bernoulli_distribution.BernoulliDistribution(p)

        self.p = p
        self.n = n

        self.r = list(range(n + 1))

        #self.dist = [self.pmf(r_val) for r_val in self.r]
        self.dist = [0] * (n + 1)

    def getData(self):
        """Return distribution"""
        for i in range(0, self.n):
            successful_trials = self.bern.getData(self.n)
            self.dist[successful_trials] += (1 / self.n)
        return self.dist


    def pmf(self, r):
        """Probability mass function"""
        return binom(self.n, r) * (self.p ** r) * ((1 - self.p) ** (self.n - r))
