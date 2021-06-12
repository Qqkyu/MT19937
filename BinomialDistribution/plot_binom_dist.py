import matplotlib.pyplot as plt
import numpy as np


class BinomDistPlot:
    """Creates plot of binomial distribution"""
    def __init__(self, binom_dist):
        """Initialize variables"""
        self.binom = binom_dist

        self.data = self.binom.getData()

    def plot(self):
        """Create and show a plot"""
        sample_binom = self.data

        x = np.arange(0, self.binom.n)

        plt.bar(x, height=sample_binom)

        plt.xlabel('Data')
        plt.ylabel('Probability')
        plt.title("Bernoulli Distribution Histogram")

        plt.xticks(x, range(0, self.binom.n))

        plt.axis(ymin=0, ymax=self.binom.p)  # x_start, x_end, y_start, y_end

        plt.show()
