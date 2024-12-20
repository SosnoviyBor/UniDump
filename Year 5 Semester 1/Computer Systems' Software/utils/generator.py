import random
import string
from sys import maxsize


random.seed(1)


def genRandomEquation(len:int) -> str:
    # ліниво, але працює
    return ''.join(random.choices(string.ascii_lowercase + string.digits + "+-*/^().", k=len))


def genRandomEqationWithValues(operatorCount:int, variableCount:int) -> str:
    operators = "+-*/^"
    
    expression = random.choice(string.ascii_lowercase[:variableCount])
    for _ in range(operatorCount):
        expression += random.choice(operators) + random.choice(string.ascii_lowercase[:variableCount])
    
    return expression