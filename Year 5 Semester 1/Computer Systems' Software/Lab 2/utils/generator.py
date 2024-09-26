import random
import string

def genRandomEquation(len:int) -> str:
    # ліниво, але працює
    return ''.join(random.choices(string.ascii_lowercase + string.digits + "+-*/^().", k=len))