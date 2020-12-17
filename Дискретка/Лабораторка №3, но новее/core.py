def hasConst0():
    n = 0
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                 if(x== 0 and y == 0 and z == 0 and F[n] == "0"):
                     return "Константу 0 зберігає"
                 n+=1
    return "Константу 0 не зберігає"

def hasConst1():
    n = 0
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (x == 1 and y == 1 and z == 1 and F[n] == "1"):
                    return "Константу 1 зберігає"
                n += 1
    return "Константу 1 не зберігає"

def isSelfdual():
    not_F = ""
    for i in range(len(F)):
        if(F[i] == "0"):
            not_F += "1"
        else:
            not_F += "0"
    not_F = not_F[::-1]
    if(F == not_F):
        return "Самодвоїста"
    else:
        return "Несамодвоїста"

def isLinear():
    global a0, a2, a3, a1, a12, a23, a13, a123
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if x == 0 and y == 0 and z == 0:
                    a0 = int(F[0])
                if x == 0 and y == 0 and z == 1:
                    a3 = linearHelp(a0,1)
                if x == 0 and y == 1 and z == 0:
                    a2 = linearHelp(a0,2)
                if x == 0 and y == 1 and z == 1:
                    a23 = linearHelp(a0^a3^a2,3)
                if x == 1 and y == 0 and z == 0:
                    a1 = linearHelp(a0,4)
                if x == 1 and y == 0 and z == 1:
                    a13 = linearHelp(a0^a1^a3,5)
                if x == 1 and y == 1 and z == 0:
                    a12 = linearHelp(a0^a1^a2,6)
                if x == 1 and y == 1 and z == 1:
                    a123 = linearHelp(a0^a1^a2^a3^a12^a13^a23,7)
    if a12 == 0 and a13 == 0 and a23 == 0 and a123 == 0:
        return "Лінійна"
    else:
        return "Нелінійна"
def linearHelp(a,n):
    for i in 0, 1:
        ax = i
        if (int(F[n]) == a ^ ax):
            return ax

def ddnf():
    n = 0
    result = ""
    result1 = ""
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if(F[n] == "1"):
                    if(x == 1):
                        result += "(x"
                    else:
                        result += "(x'"
                    if (y == 1):
                        result += "y"
                    else:
                        result += "y'"
                    if (z == 1):
                        result += "z)"
                    else:
                        result += "z')"
                    result += "+"
                n+=1
    for let in range(len(result)-1):
        result1 += result[let]
    return "ДДНФ: " + result1

def dknf():
    n = 0
    result = ""
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if(F[n] == "0"):
                    if(x == 1):
                        result += "(x'+"
                    else:
                        result += "(x+"
                    if (y == 1):
                        result += "y'+"
                    else:
                        result += "y+"
                    if (z == 1):
                        result += "z')"
                    else:
                        result += "z)"
                n+=1
    return "ДКНФ: " + result

F =  "01111000"

n = 0
print("+ — — — + — +")
print("|","x","y","z","|","F","|")
print("+ — — — + — +")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            print("|",x,y,z,"|",F[n],"|")
            n+=1
print("+ — — — + — +")

print(hasConst0())
print(hasConst1())
print(isSelfdual())
print(isLinear())
print(ddnf())
print(dknf())