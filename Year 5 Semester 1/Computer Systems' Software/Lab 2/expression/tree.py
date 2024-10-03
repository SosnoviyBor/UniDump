import graphviz


def parseExpression(expression: str):
    operator_dict = {
    'Add': {'+', '-'},
    'Mul': {'*', '/'},
    'Pow': {'^'}
    }

    def checkOperator(operators, input):
        operatorList = []
        bracket_level = 0
        for i, c in enumerate(input):
            if c == '(':
                bracket_level += 1
            elif c == ')':
                bracket_level -= 1

            elif c in operators and bracket_level == 0:
                if i == 0 and c == '-':
                    continue
                operatorList.append(i)
        
        if operatorList:
            return operatorList[len(operatorList) // 2]
        return None

    def openBrackets(input):
        bracket_level = 0
        while input[0] == '(' and input[-1] == ')':
            for i, c in enumerate(input):
                if c == '(':
                    bracket_level += 1
                elif c == ')':
                    bracket_level -= 1
                    if bracket_level == 0 and i < len(input) - 1:
                        return input
            input = input[1:-1]
        return input

    def nodeGen(input):
        input = openBrackets(input)
        for operators in ('Add', 'Mul', 'Pow'):
            idx = checkOperator(operator_dict[operators], input)
            if idx:
                symbol = input[idx]
                node = Node(symbol)
                left_child = nodeGen(input[:idx])
                right_child = nodeGen(input[idx + 1:])
                node.setChildren(left_child, right_child)
                return node

        return Node(input.strip())

    return Tree(nodeGen(expression))


class Node():

    def __init__(self, symbol):
        self.symbol = symbol
        self.id = None
        self.level = None
        self.parent = None
        self.children = tuple()


    def setChildren(self, left, right):
        self.children = (left, right)
        left.parent = self
        right.parent = self
    

    def _strSubtree(self, depth):
        # don't look at this
        # look at the console
        output = depth*'  ' + self.symbol
        if self.children:
            output += ' (\n'
            for i, child in enumerate(self.children):
                if i > 0:
                    output += ', \n'
                output += child._strSubtree(depth + 1)
            output += '\n' + depth*'  ' + '  ) '
            return output
        else:
            return '  ' + output


    def _setLevel(self, level):
        self.level = level
        for child in self.children:
            child._setLevel(level+1)


    def _setId(self, id):
        self.id = id
        for i, child in enumerate(self.children):
            child._setId(id + str(i))


    def _addNodesAndEdgesToGraph(self, graph):
        for child in self.children:
            graph.node(child.id, child.symbol)
            graph.edge(self.id, child.id)
            child._addNodesAndEdgesToGraph(graph)


class Tree():

    def __init__(self, root):
        self.root = root
        self.updateLevel()
        self.updateId()


    def printPrefix(self):
        print("\n"+
              "##### Вираз у вигляді дерева #####\n"+
              self.root._strSubtree(0))
    

    def updateLevel(self):
        self.root._setLevel(0)


    def updateId(self):
        self.root._setId('0')


    def generateGraph(self, name='graph'):
        graph = graphviz.Digraph(name)
        graph.node(self.root.id, self.root.symbol)
        self.root._addNodesAndEdgesToGraph(graph)
        return graph