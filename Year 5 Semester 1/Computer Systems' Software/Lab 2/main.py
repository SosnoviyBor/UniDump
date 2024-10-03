from expression.corrector import Corrector
from utils.generator import genRandomEquation
import expression.tree as tree

# шось графвіз тупенький якийсь
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

# expression = Corrector(genRandomEquation(100)).correct()
expression = Corrector("-a+(v+p*(6-h+b*(d+u+5+10)))").correct()

expTree = tree.parseExpression(expression)
# expTree.printPrefix()
graph = expTree.generateGraph()
graph.render(filename='graph.dot', directory='generated_graphs', view=True, format='png') 

# a*(a+b+c)-a*b+c*d+v*f
# a*(b+(c+d)/e)+b*0+5+4-1*n
# 0+b*0+0*a+a*b+1
# 2+3+4+5+6+7+8*s-p
# -a+(v+p*(6-h+b*(d+u+5+10)))