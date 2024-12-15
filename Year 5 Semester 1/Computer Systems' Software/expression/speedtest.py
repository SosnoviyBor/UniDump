import time
import sys
import re

import expression.evaluator as evaluator


sys.setrecursionlimit(100000)


def test(expression:str):
    start1 = time.perf_counter()
    resultParallel = evaluator.evaluate(expression, {}, False)
    end1 = time.perf_counter()
    
    start2 = time.perf_counter()
    resultNormal = eval(expression)
    end2 = time.perf_counter()
    
    operatorCount = len([op for op in re.findall(r'[\+\-\*\/]', expression)])
    
    print("\n"+
          "##### Порівняння способів обчислення #####\n"
          f"Довжина виразу: {operatorCount}\n"+
          f"Час багатопоточного: {end1 - start1}\n"+
          f"Час однопоточного:   {end2 - start2}")