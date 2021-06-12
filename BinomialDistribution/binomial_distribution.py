from BernoulliDistribution import bernoulli_distribution


class BinomialDistribution:
    """Generator implementing binomial distribution using Bernoulli distribution"""

    def __init__(self, p, n):
        """Initialize coefficients"""
        self.bern = bernoulli_distribution.BernoulliDistribution(p)

        self.p = p
        self.n = n

        self.r = list(range(n + 1))

        self.dist = [0] * (n + 1)

    def getData(self):
        """Return distribution"""
        for i in range(0, self.n):
            successful_trials = self.bern.getData(self.n)
            self.dist[successful_trials] += 1
        return self.dist
