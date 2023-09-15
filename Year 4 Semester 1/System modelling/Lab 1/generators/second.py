import random
import numpy as np
from scipy import integrate

from .base import GeneratorBase

class Second(GeneratorBase):
    def __init__(self, amount, intervals, a, sigma):
        self.A = a
        self.sigma = sigma
        super().__init__(amount, intervals)

    def validate(self):
        print(
            "\n### Task 2 ###\n" +
            f"Lambda: {self.A}\n" +
            f"Sigma: {self.sigma}\n" +
            "----------------------------------------------"
        )
        self._get_stats()

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
                self.limit_list[i][0],
                self.limit_list[i][1])[0]
                for i in range(self.intervals)]