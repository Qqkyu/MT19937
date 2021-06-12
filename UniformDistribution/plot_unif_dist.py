import matplotlib.pyplot as plt


class UnifDistPlot:
    """Creates plot of uniformly distributed numbers"""
    def __init__(self, unif_dist, amount=1000000, bins=100, y_end=100000):
        """Initialize variables"""
        self.unif = unif_dist

        self.low = self.unif.low
        self.high = self.unif.high

        self.amount = amount
        self.data = self.unif.getData(self.amount)

        self.bins = bins
        self.y_end = y_end

    def plot(self):
        """Create and show a plot"""
        plt.hist(self.data, self.bins)

        plt.xlabel('X~U[' + str(self.low) + ',' + str(self.high) + ']')
        plt.ylabel('Count')
        plt.title("Uniform Distribution Histogram (Bin size " + str(self.bins) + ")")
        plt.axis([self.low, self.high, 0, self.y_end])  # x_start, x_end, y_start, y_end
        plt.grid(True)

        plt.show()
