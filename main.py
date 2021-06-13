import random
import sys

import numpy as np

from MersenneTwister import MT19937
from UniformDistribution import uniform_distribution, plot_unif_dist
from BernoulliDistribution import bernoulli_distribution, plot_bern_dist
from BinomialDistribution import binomial_distribution, plot_binom_dist
from PoissonDistribution import poisson_distribution, plot_poiss_dist
from ExponentialDistribution import exponential_distribution, plot_exp_dist
from NormalDistribution import normal_distribution, plot_norm_dist


def generateFileWithRandomNums(gen, amount):
    file = open("data.txt", "w")
    file.write("#==================================================================\n")
    file.write("# Generator MT19937 seed=" + str(gen.seed) + "\n")
    file.write("#==================================================================\n")
    file.write("type: d\n")
    file.write("count: " + str(amount) + "\n")
    file.write("numbit: 32\n")
    for i in range(amount):
        file.write(str(np.uint32(gen.extractNumber())) + "\n")


if __name__ == "__main__":
    seed_val = random.randrange(sys.maxsize)
    gen = MT19937.MT19937(seed_val)
    generateFileWithRandomNums(gen, 100000000)
    #unif = uniform_distribution.UniformDistribution(0, 1)
    #unif_plot = plot_unif_dist.UnifDistPlot(unif)
    #unif_plot.plot()
    #bern = bernoulli_distribution.BernoulliDistribution(0.5)
    #bern_plot = plot_bern_dist.BernDistPlot(bern, 100000)
    #bern_plot.plot()
    #binom = binomial_distribution.BinomialDistribution(0.5, 50)
    #binom_plot = plot_binom_dist.BinomDistPlot(binom)
    #binom_plot.plot()
    #poiss = poisson_distribution.PoissonDistribution(10, 100000)
    #poiss_plot = plot_poiss_dist.PoissDistPlot(poiss)
    #poiss_plot.plot()
    #exp = exponential_distribution.ExponentialDistribution(0.5)
    #exp_plot = plot_exp_dist.ExpDistPlot(exp, 10000)
    #exp_plot.plot()
    #norm = normal_distribution.NormalDistribution(0, 1)
    #norm_plot = plot_norm_dist.NormDistPlot(norm)
    #norm_plot.plot()
    #normal_distribution.test(norm.getData(1000))
