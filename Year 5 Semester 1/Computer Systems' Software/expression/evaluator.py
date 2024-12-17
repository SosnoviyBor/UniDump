from expression.tree import Tree, Node
from utils.diagramBuilder import DiagramBuilder
from utils.consts import OPERATORS, OPERATION_SPEED


def evaluate(tree:Tree, processes:int, printDiagram:bool):
    if printDiagram:
        diagram = DiagramBuilder(processes)
        print("\n" + diagram.header())
    
    steps = 0
    
    # edgecase when there is an leaf next to the root
    for i in range(len(tree.root.children)):
        if tree.root.children[i].symbol not in OPERATORS:
            tree.root.children[i] = None
    
    # trim everything but the root
    while not all(child is None for child in tree.root.children):
        paths = traverse(tree.root)
        paths = normalizePaths(paths)
        
        # count symbols
        symbolCount = {"+": 0, "-": 0, "*": 0, "/": 0, "^": 0, }
        for path in paths:
            symbol = path[-1]["symbol"]
            symbolCount[symbol] += 1
        # find most frequent one
        mostFrequentSymbol = (None, -1)
        for symbol, count in symbolCount.items():
            if count > mostFrequentSymbol[1]:
                mostFrequentSymbol = (symbol, count)
        
        # pick symbols to evaluate
        activePaths = []
        for path in paths:
            if path[-1]["symbol"] == mostFrequentSymbol[0]:
                activePaths.append(path)
            
            if len(activePaths) == processes:
                break
        
        # trim the tree
        for path in activePaths:
            evalNode(tree.root, path)
        # count the steps
        steps += OPERATION_SPEED[mostFrequentSymbol[0]] * len(activePaths)
        
        # print diagram
        if printDiagram:
            print(diagram.body(mostFrequentSymbol[0], len(activePaths)))
    
    # count the steps
    steps += OPERATION_SPEED[tree.root.symbol]
    
    # print diagram
    if printDiagram:
        print(diagram.body(tree.root.symbol, 1))
        print(diagram.bottom())
    
    return steps


def traverse(root:Node):
    # thanks neuro-sama
    def dfs(node:Node, path:list, allPaths:list, direction:int):
        if not node:
            return
        # Add the current node's value to the path
        path.append({
            "symbol": node.symbol,
            "direction": direction})
        
        # If the current node is a leaf, append the path to all_paths
        if not node.children or all(child is None for child in node.children):
            allPaths.append(list(path))
        else:
            # Recur for the left and right subtrees
            dfs(node.children[0], path, allPaths, 0)
            dfs(node.children[1], path, allPaths, 1)
        
        # Backtrack to explore other paths
        path.pop()

    all_paths = []
    dfs(root, [], all_paths, -1)
    
    return all_paths


def normalizePaths(allPaths:list):
    trimmedPaths = []
    # trimming leaves
    for path in allPaths:
        if path[-1]["symbol"] not in OPERATORS:
            path.pop()
        if path not in trimmedPaths:
            trimmedPaths.append(path)

    # sort paths from longest to shortest
    trimmedPaths.sort(key=lambda path: len(path), reverse=True)
    
    # deleting subpaths
    validPaths = [trimmedPaths[0]]
    for currentPath in trimmedPaths[1:]:
        for validPath in validPaths:
            # list of dicts compare hack my ass
            if str(currentPath)[1:-1] in str(validPath):
                break
        else:
            if currentPath not in validPaths:
                validPaths.append(currentPath)
    
    return validPaths


def evalNode(node:Node, path:list):
    childDir = path.pop(1)["direction"]
    if len(path) > 1:
        evalNode(node.children[childDir], path)
    else:
        node.children[childDir] = None