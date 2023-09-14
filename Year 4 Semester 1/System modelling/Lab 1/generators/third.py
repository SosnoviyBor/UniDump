import random
import math
import numpy as np
import statistics as stats

import utils

class Third():
    def __init__(self, amount, intervals, a, c):
        self.A = a
        self.C = c
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
            "\n### Task 3 ###\n" +
            f"A: 5^{round(math.log(self.A, 5))} or {self.A}\n" +
            f"C: 2^{round(math.log(self.C, 2))} or {self.C}\n" +
            "----------------------------------------------"
        )
        utils.get_stats(self)

    def _gen_dist(self):
        z = self.A * random.random() % self.C
        dist = []
        for _ in range(self.amount):
            z = self.A * z % self.C
            val = z / self.C
            dist.append(val)
        return np.array(dist)
    
    def _gen_perfect_dist(self):
        return [(self.interval_list[i][1] - self.interval_list[i][0]) /
                (max(self.generated_dist) - min(self.generated_dist))
                for i in range(self.intervals)]