from matplotlib import pyplot

import generators

INTERVALS = 15
GENERATED_AMOUNT = 10_000
# first
A1 = 0.5
# second
A2 = 1
SIGMA = 1
# third
A3 = pow(5, 13)
C3 = pow(2, 31)

GENERATOR = 2

def main():
    match GENERATOR:
        case 1: dist = generators.first.First(GENERATED_AMOUNT, INTERVALS, A1)
        case 2: dist = generators.second.Second(GENERATED_AMOUNT, INTERVALS, A2, SIGMA)
        case 3: dist = generators.third.Third(GENERATED_AMOUNT, INTERVALS, A3, C3)
        case _: return
    dist.validate()

if __name__ == "__main__":
    main()