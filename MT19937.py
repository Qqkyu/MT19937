from UniformDistribution import uniform_distribution, plot_unif_dist
from BernoulliDistribution import bernoulli_distribution, plot_bern_dist


class MT19937:
    """Mersenne Twister standard implementation (MT19937)"""

    def __init__(self, seed):
        """Initialize standard coefficients for MT19937"""

        # w: word size (in number of bits)
        self.w = 32

        # n: degree of recurrence
        self.n = 624

        # m: middle word, an offset used in the recurrence relation defining the series x, 1 <= m < n
        self.m = 397

        # r: separation point of one word, or the number of bits of the lower bitmask, 0 <= r <= w - 1
        self.r = 31

        # a: coefficients of the rational normal form twist matrix
        self.a = 2567483615  # 0x9908B0DF

        # u,d,l: additional Mersenne Twister tempering bit shifts / masks
        self.u = 11
        self.d = 4294967295  # 0xFFFFFFFF
        self.l = 18

        # s,t: tempering bit shifts
        self.s = 7
        self.t = 15

        # b,c: tempering bitmasks
        self.b = 2636928640  # 0x9D2C5680
        self.c = 4022730752  # 0xEFC60000

        # f: generator parameter
        self.f = 1812433253

        # Auxiliary constants
        self.RAND_MAX = 2 ** self.w - 1
        self.RAND_MIN = 0

        # -- Miscellaneous variables -- #

        # Array of length n to store the state of the generator
        self.MT = []
        self.index = self.n + 1

        self.lower_mask = (1 << self.r) - 1
        # lowest w bits - ((1 << w) - 1) is a mask to isolate w bits
        self.upper_mask = (~self.lower_mask) & ((1 << self.w) - 1)

        # -- Initialize generator from a seed -- #
        self.index = self.n
        self.MT.append(seed)
        for i in range(1, self.n):
            mask = (1 << self.w) - 1  # mask to isolate w bits
            self.MT.append((self.f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (self.w - 2))) + i) & mask)

    def extractNumber(self):
        """Extract a tempered value based on MT[index]"""
        if self.index >= self.n:
            if self.index > self.n:
                raise RuntimeError("Generator was never seeded")
            self.generateNumbers()

        y = self.MT[self.index]
        y ^= ((y >> self.u) & self.d)
        y ^= ((y << self.s) & self.b)
        y ^= ((y << self.t) & self.c)
        y ^= (y >> self.l)

        self.index += 1
        return y & ((1 << self.w) - 1)

    def generateNumbers(self):
        """Generate the next n values from the series x_i"""
        for i in range(0, self.n):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i + 1) % self.n] & self.lower_mask)
            xa = x >> 1
            if x % 2 != 0:
                xa = xa ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xa

        self.index = 0

    def randomUnif(self):
        return self.extractNumber() / 2 ** self.w


if __name__ == "__main__":
    #unif = uniform_distribution.UniformDistribution(1, 2)
    #unif_plot = plot_unif_dist.UnifDistPlot(unif)
    #unif_plot.plot()
    bern = bernoulli_distribution.BernoulliDistribution(0.5)
    bern_plot = plot_bern_dist.BernDistPlot(bern, 100000)
    bern_plot.plot()
