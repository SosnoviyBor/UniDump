import itertools
import re


def comutate(expression:str, log:bool = True):
    if not expression.startswith("-"):
        expression = "+" + expression
    
    expressionParts = [part for part in re.split(r"([+-][a-zA-Z0-9*/^.]*)", expression) if part != ""]
    
    i = 1
    if log: print("##### Результат комутації #####")
    for perm in itertools.permutations(expressionParts):
        variant = "".join(perm)
        
        if variant.startswith("+"):
            variant = variant[1:]
            
        if log:
            print(f"№{i} -> {variant}")
            i += 1
    
        yield variant