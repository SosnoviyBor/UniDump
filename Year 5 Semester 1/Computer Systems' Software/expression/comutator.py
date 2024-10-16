import itertools
import re

import utils.coloring as coloring


def comutate(expression:str):
    if not expression.startswith("-"):
        expression = "+" + expression
    
    expressionParts = [part for part in re.split(r"([+-][a-zA-Z0-9*/^]*)", expression) if part != ""]
    expressionPermutations = list(itertools.permutations(expressionParts))
    
    expressionVariants = []
    for perm in expressionPermutations:
        variant = "".join(perm)
        
        if variant.startswith("+"):
            variant = variant[1:]
            
        expressionVariants.append(variant)
    
    print("\n" +
          "##### Комутаційне перетворення #####\n" +
          "##### Частини виразу #####\n" +
          f"{coloring.wrap('  '.join(expressionParts), coloring.Color.Foreground.CYAN)}\n" +
          "##### Результат комутації #####")
    for variant in expressionVariants:
        print(variant)
    
    return expressionVariants