import multiprocessing as mp
import re

import utils.coloring as coloring
import utils.atomic as atomic

# fuck python multiprocessing


def evaluate(expression:str, params:dict):
    manager = mp.Manager()
    expression = subtitude(expression, params)
    
    # the only way i could deduce if it's an actual number or not without try except
    # yes, the default methods all break when provided negative float
    # yes, its hella stupid https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth
    while re.findall(r"[\+\-\*\/\^]+", re.sub(r"^-", "", expression)):
        subexpressions = prepareSubexpressions(expression)
    
        pool = mp.Pool(6)
        poolResult = manager.list({})
        
        args = []
        for subexp in subexpressions:
            args.append((subexp, poolResult))
        pool.map(evaluateSubexpressions, args)
        
        pool.close()
        pool.join()
    
    return expression


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


def prepareSubexpressions(expression:str):
    operators = ["^", "*", "/", "+", "-"]
    subexpressions = []
    operatorCount = 0
    maxOperators = 6
    
    for operator in operators:
        if operator in expression:
            
            tokens = [part for part in re.split(r"([\+\-\*\/\^])", expression) if part != ""]
            
            for i in range(len(tokens)):
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
                        
                        operatorCount += 1
                        if operatorCount == maxOperators:
                            break
                        
                    subexpressions.append(subexpression)
                        
                if operatorCount == maxOperators:
                    break
            
            break
    
    return subexpressions


def evaluateSubexpressions(args):
    subexpression, poolResult = args
    poolResult[subexpression] = eval(subexpression)