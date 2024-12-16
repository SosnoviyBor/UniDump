from expression.tree import Tree


operators = "^*/+-"
opearationSpeed = {
    "+": 1,
    "-": 3,
    "*": 4,
    "/": 8,
    "^": 4
}


def evaluate(tree:Tree, processes:int):
    while not tree.root.symbol.isdecimal():
        pass


def traverse(tree:Tree):
    pass