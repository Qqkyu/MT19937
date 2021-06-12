from UniformDistribution import uniform_distribution


class BernoulliDistribution:
    """Generator implementing Bernoulli distribution using uniform distribution"""

    def __init__(self, p):
        """Initialize MT19937 and coefficients"""
        self.unif = uniform_distribution.UniformDistribution(0, 1)
        self.p = p

    def extractNumber(self):
        number = self.unif.extractNumber()
        return number < self.p

    def getData(self, amount):
        """Return number of successful trials"""
        successful_trials = 0
        for i in range(0, amount):
            successful_trials += self.extractNumber()
        return successful_trials
