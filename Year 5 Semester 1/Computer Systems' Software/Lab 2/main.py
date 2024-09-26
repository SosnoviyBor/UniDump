from expression.corrector import Corrector
from utils.generator import genRandomEquation
import expression.tree as tree

# шось графвіз тупенький якийсь
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

# expression = Corrector(genRandomEquation(100)).correct()
expression = Corrector("(A+B)+C/D+G*(K/L+M+N)").correct()
# expression = Corrector("((52345.01+312,2)*b)").correct()

expTree = tree.parseExpression(expression)
expTree.printPrefix()
graph = expTree.generateGraph()
graph.render(filename='graph.dot', directory='generated_graphs', view=True, format='png') 

# cos(g)*a+5+c*d+e-d*f3/avc_1
# (a+b)+func((a*baa+1bj_ko*(j-c))
# -a+b2
# g1+(a+2.3))+(6-sin(5)
# ((52345.01+312,2)*b)