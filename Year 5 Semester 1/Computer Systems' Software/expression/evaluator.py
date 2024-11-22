import multiprocessing as mp
import re

import utils.coloring as coloring
import utils.atomic as atomic

# fuck python multiprocessing


def evaluate(expression:str, params:dict):
    operators = ["^", "*", "/", "+", "-"]
    expression = subtitude(expression, params)
    manager = mp.Manager()
    
    for operator in operators:
        pool = mp.Pool(processes=6, initializer=initPool, initargs=[mp.Lock()])
        syncedExpression = manager.list(expression)
        counter = atomic.Int()
        
        pool.map(evaluateByOperator, ((syncedExpression, counter, operator),))
        
        pool.close()
        pool.join()
    
    return expression


def initPool(initLock):
    global lock
    lock = initLock


def subtitude(expression:str, params:dict) -> str:
    for k, v in params.items():
        expression = expression.replace(k, str(v))
    
    coloredExpression = expression
    variables = re.findall(r"[a-zA-Z]+", coloredExpression)
    for var in variables:
        coloredExpression = re.sub(var, coloring.wrap(var, coloring.Color.Foreground.RED), coloredExpression)
    print("\n" +
          "##### Вираз зі значеннями #####\n" +
         f"{coloredExpression}")
    
    assert not variables
    
    return expression


def evaluateByOperator(args):
    expression, counter, operator = args
    
    tokens = [part for part in re.split(r"([\+\-\*\/\^])", str(expression)) if part != ""]
    subexpression = None
    
    while operator in expression:
        with lock:
            # trust noone, even yourself
            if (operator not in expression or
                # if that's the single negative number
                re.findall(r"[\+\-\*\/\^]+", re.sub(r"^-", "", str(expression)))):
                break
            
            while i := counter.get() < len(tokens):
                if tokens[i] == operator:
                    # the only time when minus at the start matters
                    if i == 2 and tokens[0] == "-":
                        subexpression = "-"
                    else:
                        subexpression = ""
                    
                    subexpression += tokens[i-1]
                    # суслік operator appending
                    # for when there are same operators placed back to back
                    while tokens[i] == operator:
                        subexpression += tokens[i]
                        subexpression += tokens[i+1]
                        
                        i += 2
                
                counter.inc()
            
        subexpressionValue = eval(subexpression)
        
        with lock:
            expression.replace(subexpression, subexpressionValue)