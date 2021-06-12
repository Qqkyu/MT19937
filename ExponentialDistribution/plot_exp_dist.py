import matplotlib.pyplot as plt


class ExpDistPlot:
    """Creates plot of exponentially distributed numbers"""
    def __init__(self, exp_dist, amount=1000000):
        """Initialize variables"""
        self.exp = exp_dist

        self.amount = amount
        self.data = self.exp.getData(amount)

        self.bins = int(amount / 10)

    def plot(self):
        """Create and show a plot"""
        plt.hist(self.data, self.bins)

        plt.xlabel('X~Exp[' + str(self.exp.lmbd) + ']')
        plt.ylabel('Count')
        plt.title("Exponential Distribution Histogram")

        plt.grid(True)

        plt.show()
