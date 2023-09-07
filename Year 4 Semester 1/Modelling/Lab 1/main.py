from matplotlib import pyplot

import generators

GENERATED_AMOUNT = 10_000
# first
LAMBDA = 10
# second
A2 = 1
SIGMA = 1
# third
A3 = 5**13
C3 = 2**31
Z0 = 5
nums = []

while True:
    inp = 3
    match inp:
        case 1:
            generated, perfect = generators.first(GENERATED_AMOUNT, LAMBDA)
            pyplot.hist(generated, 200, alpha=0.5, label='generated')
            break
        case 2:
            generated, perfect = generators.second(GENERATED_AMOUNT, A2, SIGMA)
            pyplot.hist(generated, 200, alpha=0.5, label='generated')
            pyplot.hist(perfect, 200, alpha=0.5, label='perfect')
            break
        case 3:
            generated, perfect = generators.third(GENERATED_AMOUNT, A3, C3, Z0)
            pyplot.hist(generated, 200, alpha=0.5, label='generated')
            pyplot.hist(perfect, 200, alpha=0.5, label='perfect')
            break
        case _:
            pass

pyplot.legend(loc='upper right')
pyplot.show()