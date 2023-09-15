import random
import numpy as np

from .base import GeneratorBase

class First(GeneratorBase):
    def __init__(self, amount, intervals, a):
        self.A = a
        super().__init__(amount, intervals)

    def validate(self):
        print(
            "\n### Task 1 ###\n" +
            f"Lambda: {self.A}\n" +
            "----------------------------------------------"
        )
        self._get_stats()

    def _gen_dist(self):
        dist = []
        for _ in range(self.amount):
            val = -np.log(random.random()) / self.A
            dist.append(val)
        return np.array(dist)
    
    def _gen_perfect_dist(self):
        return [np.exp(-self.A * self.limit_list[i][0]) -
                np.exp(-self.A * self.limit_list[i][1])
                for i in range(self.intervals)]