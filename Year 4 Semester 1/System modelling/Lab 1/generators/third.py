import random
import math
import numpy as np

from .base import GeneratorBase

class Third(GeneratorBase):
    def __init__(self, amount, intervals, a, c):
        self.A = a
        self.C = c
        super().__init__(amount, intervals)

    def validate(self):
        print(
            "\n### Task 3 ###\n" +
            f"A: 5^{round(math.log(self.A, 5))} or {self.A}\n" +
            f"C: 2^{round(math.log(self.C, 2))} or {self.C}\n" +
            "----------------------------------------------"
        )
        self._get_stats()

    def _gen_dist(self):
        z = self.A * random.random() % self.C
        dist = []
        for _ in range(self.amount):
            z = self.A * z % self.C
            val = z / self.C
            dist.append(val)
        return np.array(dist)
    
    def _gen_perfect_dist(self):
        return [(self.limit_list[i][1] - self.limit_list[i][0]) /
                (max(self.generated_dist) - min(self.generated_dist))
                for i in range(self.intervals)]