import matplotlib.pyplot as plt
import numpy as np


class PoissDistPlot:
    """Creates plot of Poisson distribution"""
    def __init__(self, poiss_dist):
        """Initialize variables"""
        self.poiss = poiss_dist

        self.data = self.poiss.getData()

        self.cut_point = 0.01

    def plot(self):
        """Create and show a plot"""
        sample_poisson = self.data

        max_value = max(sample_poisson)

        plot_arr = [0] * (max_value + 1)

        for i in range(0, len(sample_poisson)):
            plot_arr[sample_poisson[i]] += 1

        x = np.arange(0, max_value + 1)

        plt.bar(x, height=plot_arr)

        plt.xlabel('X~Poiss[' + str(self.poiss.lmbd) + ']')
        plt.ylabel('Count')
        plt.title("Poisson Distribution Histogram")

        plt.axis(ymin=0, ymax=max(plot_arr) + max(plot_arr) / 10)  # x_start, x_end, y_start, y_end

        plt.show()
