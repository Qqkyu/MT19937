import matplotlib.pyplot as plt
import numpy as np


class BernDistPlot:
    """Creates plot of Bernoulli distribution"""
    def __init__(self, bern_dist, amount=1000):
        """Initialize variables"""
        self.bern = bern_dist

        self.amount = amount
        self.data = self.bern.getData(self.amount)

    def plot(self):
        """Create and show a plot"""
        sample_bernoulli = self.data

        x = np.arange(2)

        plt.bar(x, height=[self.amount - sample_bernoulli, sample_bernoulli])

        plt.xlabel('X~Bern(' + str(self.bern.p) + ')')
        plt.ylabel('Count')
        plt.title("Bernoulli Distribution Histogram")

        plt.xticks(x, ['0', '1'])

        plt.axis(ymin=0, ymax=self.amount)  # x_start, x_end, y_start, y_end

        plt.show()
