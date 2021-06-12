from BernoulliDistribution import bernoulli_distribution

import math


def binom(n, k):
    """Calculates binomial coefficient"""
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))


class BinomialDistribution:
    """Generator implementing binomial distribution using Bernoulli distribution"""

    def __init__(self, p, n):
        """Initialize MT19937 and coefficients"""
        self.bern = bernoulli_distribution.BernoulliDistribution(p)

        self.p = p
        self.n = n

        self.r = list(range(n))

        self.dist = [self.pmf(r_val) for r_val in self.r]

    def getData(self):
        """Return distribution"""
        return self.dist

    def pmf(self, r):
        """Probability mass function"""
        return binom(self.n, r) * (self.p ** r) * ((1 - self.p) ** (self.n - r))
