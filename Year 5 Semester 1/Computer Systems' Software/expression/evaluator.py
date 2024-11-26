import multiprocessing as mp
import re

import utils.coloring as coloring


def evaluate(expression:str, params:dict):
    print("\n" +
          "##### Обчислення виразу #####")
    
    manager = mp.Manager()
    expression = subtitude(expression, params)
    
    for operator in ["^", "*", "/", "+", "-"]:
        args = []
        pool = mp.Pool(6)
        poolResult = manager.dict({})
        subexpressions = prepareSubexpressions(expression, operator)
        # argument preparation for parallel function
        for subexp in subexpressions:
            args.append((subexp, poolResult))
        # threading itself
        # kinda slow to boot, tbh
        pool.map(evaluateSubexpressions, args)
        pool.close()
        pool.join()
        # result parsing
        for old, new in dict(poolResult).items():
            expression = expression.replace(old, str(new))
        # logging
        print(f"Обчислення {operator}   ->   {expression}")
    # more logging
    print("##### Кінцевий результат #####\n" +
         f"{coloring.wrap(expression, coloring.Color.Foreground.GREEN)}")
    return expression


def subtitude(expression:str, params:dict) -> str:
    # basically thats it
    for k, v in params.items():
        expression = expression.replace(k, str(v))
    # coloring output in case if threres any variablrs left in the expression
    coloredExpression = expression
    variables = re.findall(r"[a-zA-Z]+", coloredExpression)
    for var in variables:
        coloredExpression = re.sub(var, coloring.wrap(var, coloring.Color.Foreground.RED), coloredExpression)
    print("##### Вираз зі значеннями #####\n" +
         f"{coloredExpression}")
    # check if there are any variables left
    assert not variables
    
    return expression


def prepareSubexpressions(expression:str, operator:str):
    subexpressions = []
    
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
                    if i >= len(tokens):
                        break
                    
                subexpressions.append(subexpression)
    
    return subexpressions


def evaluateSubexpressions(args):
    # IM GONNA MULTITHREAD THE FUCK OUT OF THIS eval() FUNCTION
    subexpression, poolResult = args
    poolResult[subexpression] = eval(subexpression)