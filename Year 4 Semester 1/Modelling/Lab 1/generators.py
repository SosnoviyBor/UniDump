import math
import random
import numpy as np

import validators

def first(amount, a):
    normal_dist = np.random.uniform(0,1,amount)
    mapped_nums = list(map(lambda x: -1/a * math.exp(x),
                           normal_dist))
    get_stats(normal_dist)
    exponential_dist = validators.exponential(mapped_nums, a)
    return mapped_nums, exponential_dist

def second(amount, a, sigma):
    nums = []
    for _ in range(amount):
        ui = sum(np.random.uniform(0,1,12)) - 6
        xi = sigma * ui + a
        nums.append(xi)
    get_stats(nums)
    normal_dist = validators.normal(nums, a, sigma)
    return nums, normal_dist

def third(amount, a, c, z):
    nums = []
    for _ in range(amount):
        z = (a * z) % c
        xi = z / c
        nums.append(xi)
    get_stats(nums)
    uniform_dist = validators.uniform(nums)
    return nums, uniform_dist

def get_stats(nums):
    mean = np.mean(nums)
    std = np.std(nums)
    print(f"{mean = }, {std = }")