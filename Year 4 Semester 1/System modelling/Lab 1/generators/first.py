import random
import numpy as np
import statistics as stats

import utils

class First():
    def __init__(self, amount, intervals, a):
        self.A = a
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
            "\n### Task 1 ###\n" +
            f"Lambda: {self.A}\n" +
            "----------------------------------------------"
        )
        utils.get_stats(self)

    def _gen_dist(self):
        dist = []
        for _ in range(self.amount):
            val = -np.log(random.random()) / self.A
            dist.append(val)
        return np.array(dist)
    
    def _gen_perfect_dist(self):
        return [np.exp(-self.A * self.interval_list[i][0]) - \
                np.exp(-self.A * self.interval_list[i][1])
                for i in range(self.intervals)]