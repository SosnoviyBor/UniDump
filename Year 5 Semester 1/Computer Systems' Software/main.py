from expression.corrector import Corrector
import expression.tree as tree
import expression.associator as associator
import expression.comutator as comutator
from utils.generator import genRandomEquation

# шось графвіз тупенький якийсь
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

""" Lab 1 (required) """
# expression = Corrector(genRandomEquation(100)).correct()
expression = Corrector("2+3+4+5+6+7+8*s-p").correct()

""" Lab 3 """
# expression = associator.associate(expression)

""" Lab 4 """
expressions = comutator.comutate(expression)

""" Lab 2 """
# expTree = tree.parseExpression(expression)
# expTree.printPrefix()
# graph = expTree.generateGraph()
# graph.render(filename='graph.dot', directory='generated_graphs', view=True, format='png') 

# a*(a+b+c)-a*b+c*d+v*f
# a*(b+(c+d)/e)+b*0+5+4-1*n
# 0+b*0+0*a+a*b+1
# 2+3+4+5+6+7+8*s-p
# -a+(v+p*(6-h+b*(d+u+5+10)))