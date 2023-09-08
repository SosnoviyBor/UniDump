import math
import random
import scipy.stats as stats
import numpy as np

def exponential(observed_data, a):
    exponential_dist = [1 - math.exp(1) ** (random.random() * a)
                        for _ in range(len(observed_data))]
    chi = stats.chisquare(observed_data, exponential_dist)
    p_validator(chi.pvalue, "експоненційно")
    return exponential_dist

def normal(observed_data, a, sigma):
    # tmp = []
    # for _ in range(len(observed_data)):
    #     p1 = 1
    #     p2 = sigma * math.sqrt(2*math.pi)
    #     p3 = -((random.random() - a)**2)
    #     p4 = 2 * (sigma**2)
    #     val = (p1 / p2) * math.exp(p3 / p4)
    #     tmp.append(val)
    normal_dist = np.random.normal(a,sigma,len(observed_data))
    # chi = stats.chisquare(observed_data, normal_dist)
    # p_validator(chi.pvalue, "нормально")
    return normal_dist

def uniform(observed_data):
    uniform_dist = np.random.uniform(0,1,len(observed_data))
    # chi = stats.chisquare(observed_data, uniform_dist)
    # p_validator(chi.pvalue, "рівномірно")
    return uniform_dist

def p_validator(p, type):
    if p > 0.05:
        print(f"✔️  Розподіл Є {type} розподіленим\n"+
              f"{p = }")
    else:
        print(f"❌  Розподіл НЕ Є {type} розподіленим\n"+
              f"{p = }")