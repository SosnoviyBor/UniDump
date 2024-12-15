import random
import string
from sys import maxsize


random.seed(1)


def genRandomEquation(len:int) -> str:
    # ліниво, але працює
    return ''.join(random.choices(string.ascii_lowercase + string.digits + "+-*/^().", k=len))


def genRandomEqationWithValues(operatorCount:int, high:float, rounding:int = maxsize) -> str:
    operators = "+-*/"
    
    expression = str(round(random.uniform(0, high), rounding))
    
    for _ in range(operatorCount):
        expression += str(random.choice(operators))
        # avoid division by zero
        if expression[-1] == "/":
            expression += str(round(random.uniform(1, high), rounding))
        else:
            expression += str(round(random.uniform(0, high), rounding))
    
    return expression