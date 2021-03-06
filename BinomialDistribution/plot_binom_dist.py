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

        x = np.arange(0, self.binom.n + 1)

        plt.bar(x, height=sample_binom)

        plt.xlabel('X~Binom[' + str(self.binom.n) + ',' + str(self.binom.p) + ']')
        plt.ylabel('Count')
        plt.title("Binomial Distribution Histogram")

        plt.axis(ymin=0, ymax=max(sample_binom) + max(sample_binom) / 10)  # x_start, x_end, y_start, y_end

        plt.show()
