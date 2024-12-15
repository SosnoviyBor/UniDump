import multiprocessing as mp
import re

import utils.coloring as coloring


processes = 6
operators = ["^", "*", "/", "+", "-"]
opearationSpeed = {
    "+": 1,
    "-": 3,
    "*": 4,
    "/": 8,
    "^": 4
}


def evaluate(expression:str, params:dict, log=True):
    print("\n" +
          "##### Обчислення виразу #####")
    
    manager = mp.Manager()
    expression = subtitude(expression, params)
    subexpressionsLog = []
    
    for operator in operators:
        # i SHOULD'VE BEEN a recursion, but I couldn't be bothered to rewrite it
        # spaghetti it is
        while True:
            subexpressions = prepareSubexpressions(expression, operator)
            # in case current operator is not present in the expression
            if subexpressions:
                args = []
                pool = mp.Pool(processes)
                poolResult = manager.dict({})
                
                subexpressionsLog.extend(subexpressions)
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
                # just in case
                expression = expression.replace("--", "+").replace("+-", "-")
                
                # logging
                if log: print(f"Обчислення {operator}   ->   {expression}")
            else:
                break
    # more logging
    if log: printDiagram(subexpressionsLog, processes)
    print("##### Кінцевий результат #####\n" +
         f"{coloring.wrap(expression, coloring.Color.Foreground.GREEN)}")
    return expression


def subtitude(expression:str, params:dict) -> str:
    if not params:
        return expression
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
        
        i = 0
        for _ in range(len(tokens)):
            # i dont even care anymore
            i += 1
            if i >= len(tokens):
                break
            
            if (tokens[i] == operator
                and not tokens[i-3][-1] == "e"):
                # the only time when minus at the start matters
                if i == 2 and tokens[0] == "-":
                    subexpression = "-"
                else:
                    subexpression = ""
                
                subexpression += tokens[i-1]
                
                # scientific notation support
                if subexpression[-1] == "e":
                    subexpression += tokens[i]
                    subexpression += tokens[i+1]
                    i += 2
                
                # суслік operator appending
                # for when there are same operators placed back to back
                while tokens[i] == operator:
                    subexpression += tokens[i]
                    subexpression += tokens[i+1]
                    
                    # scientific notation support
                    if subexpression[-1] == "e":
                        i += 2
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
    
    try:
        val = eval(subexpression)
    except ZeroDivisionError:
        # 0.0000000001 = 1 * 10^(-10)
        val = eval(subexpression.replace("/0", "/0.0000000001"))
    
    poolResult[subexpression] = val


def printDiagram(subexpressions, processes):
    print("##### Діаграма Ганта #####")
    
    row = 1
    
    for operator in operators:
        operatorCount = 0

        for subexpression in subexpressions:
            operatorCount += subexpression.count(operator)
        
        while operatorCount > 0:
            if operatorCount > processes:
                template = "[{op}] " * processes
                for _ in range(opearationSpeed[operator]):
                    rowNumber = str(row).ljust(4)
                    rowDiagram = template.format(op = operator)
                    print(rowNumber + rowDiagram)
                    row += 1
                operatorCount -= processes
            else:
                template = ("[{op}] " * operatorCount) + ("[ ] " * (processes - operatorCount))
                for _ in range(opearationSpeed[operator]):
                    rowNumber = str(row).ljust(4)
                    rowDiagram = template.format(op = operator)
                    print(rowNumber + rowDiagram)
                    row += 1
                break