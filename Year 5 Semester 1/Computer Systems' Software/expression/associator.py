import re

import utils.coloring as coloring


def associate(expression:str, doPrint:bool):
    expression = simplify(splitter(expression))
    
    result = ""
    for i in range(len(expression)):
        token = expression[i]
        if type(token) is list:
            result += "".join(token)
        else:
            result += token
    
    # cosmetic stuff
    tmp = ""
    for i in range(len(result)):
        if result[i] == "(":
            tmp = tmp[:-2]
            if result[i-3] == "/":
                tmp = tmp[:-2]
                tmp += coloring.wrap(result[i-4:i-2], coloring.Color.Foreground.GREEN)
            tmp += coloring.wrap(result[i-2:i+1], coloring.Color.Foreground.GREEN)
        else:
            tmp += result[i]
    tmp = tmp.replace(")", coloring.wrap(")", coloring.Color.Foreground.GREEN))
    
    if doPrint:
        print("\n"+
            "##### Результат асоціації #####\n"+
            f"{tmp}"
        )
    
    return result


def splitter(expression:str) -> list[str|list[str]]:
    newExpression = re.split(r"([+-])", expression)
    
    # by +-
    # append minus to value if needed
    if newExpression[0] == "":
        newExpression.pop(0)
        newExpression.pop(0)
        newExpression[0] = "-" + newExpression[0]
    
    # by */
    for i in range(len(newExpression)):
        if "*" in newExpression[i] or "/" in newExpression[i]:
            newExpression[i] = re.split(r"([*/()])", newExpression[i])
    
    return newExpression


def simplify(expression:list[str|list[str]]) -> list[str|list[str]]:
    rightmostBracketIndex = [i for i, token in enumerate(expression) if token == ")"]
    if not rightmostBracketIndex or rightmostBracketIndex == len(expression) - 1:
        start = 0
    else:
        start = rightmostBracketIndex.pop() + 1
        
    sameToken = None
    for i in range(start, len(expression)):
        if type(expression[i]) is list:
            currSubexp = expression[i]
            
            for j in range(i+1, len(expression)):
                if type(expression[j]) is list:
                    conseqSubex = expression[j]
                    
                    if sameToken:
                        deleteSameTokens(expression, sameToken, i)
                        continue
                    
                    for k in range(len(currSubexp)):
                        if currSubexp[k] not in "*/()" and currSubexp[k] in conseqSubex:
                            sameToken = currSubexp[k]
                            break
                    
                    deleteSameTokens(expression, sameToken, i)
                    
            if sameToken:
                break
    
    if sameToken:
        return simplify(expression)
    
    return expression


def deleteSameTokens(expression:list, token, searchAfter):
    leftmostIndex = None
    rightmostIndex = None
    symbol = None
    
    for i in range(searchAfter, len(expression)):
        if type(expression[i]) is list:
            currSubexp = expression[i]
            
            if token in currSubexp:
                # add left part
                if leftmostIndex == None:
                    leftmostIndex = i
                
                rightmostIndex = i + 1
                # remove subexpression values
                if currSubexp.index(token) == 0:
                    symbol = currSubexp.pop(0)
                    currSubexp.pop(0)
                elif currSubexp.index(token) == len(currSubexp):
                    currSubexp.pop()
                else:
                    symbol = currSubexp.pop(currSubexp.index(token) - 1)
                    currSubexp.pop(currSubexp.index(token))
    
    if rightmostIndex:
        expression.insert(rightmostIndex, ")")
        expression.insert(leftmostIndex, "(")
        expression.insert(leftmostIndex, "*")
        expression.insert(leftmostIndex, token)
        if symbol == "/":
            expression.insert(leftmostIndex, "/")
            expression.insert(leftmostIndex, "1")
        
        innerExpression = ""
        for i in range(leftmostIndex + 3, rightmostIndex + 3):
            token = expression[i]
            if type(token) is list:
                innerExpression += "".join(token)
            else:
                innerExpression += token
                
        # replace inner part
        if innerExpression:
            del expression[leftmostIndex + 3 : rightmostIndex + 3]
            expression[leftmostIndex + 3 : leftmostIndex + 3] = simplify(splitter(innerExpression))