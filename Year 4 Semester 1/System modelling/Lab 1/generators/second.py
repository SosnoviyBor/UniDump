import random
import numpy as np
import statistics as stats
from scipy import integrate

import utils

class Second():
    def __init__(self, amount, intervals, a, sigma):
        self.A = a
        self.sigma = sigma
        self.amount = amount
        self.intervals = intervals
        
        self.generated_dist = self._gen_dist()

        self.average = stats.mean(self.generated_dist)
        self.dispersion = stats.pvariance(self.generated_dist)
        self.entries = utils.gen_intervals(self.generated_dist, self.intervals)
        self.interval_list = utils.gen_interval_list(self.entries, self.intervals)
        
        self.perfect_dist = self._gen_perfect_dist()

    def validate(self):
        print(
            "\n### Task 2 ###\n" +
            f"Lambda: {self.A}\n" +
            f"Sigma: {self.sigma}\n" +
            "----------------------------------------------"
        )
        utils.get_stats(self)

    def _gen_dist(self):
        dist = []
        for _ in range(self.amount):
            mu = -6
            for _ in range(12):
                mu += random.random()
            val = self.sigma * mu + self.A
            dist.append(val)
        return np.array(dist)
    
    def _gen_perfect_dist(self):
        return [integrate.quad(
                lambda x: 1 / (self.sigma * np.sqrt(2 * np.pi)) * np.exp(- pow((x - self.A),2) / (2 * pow(self.sigma,2))),
                self.interval_list[i][0], self.interval_list[i][1])[0]
                for i in range(self.intervals)]