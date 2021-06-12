import matplotlib.pyplot as plt


class NormDistPlot:
    """Creates plot of normally distributed numbers"""
    def __init__(self, norm_dist, amount=100000):
        """Initialize variables"""
        self.norm = norm_dist

        self.amount = amount
        self.data = self.norm.getData(amount)

        self.bins = int(amount / 10)

    def plot(self):
        """Create and show a plot"""
        plt.hist(self.data, self.bins)

        plt.xlabel('X~Norm[' + str(self.norm.mu) + ',' + str(self.norm.sigma) + ']')
        plt.ylabel('Count')
        plt.title("Normal Distribution Histogram")

        plt.grid(True)

        plt.show()
