from expression.corrector import Corrector
import expression.tree as tree
import expression.associator as associator
import expression.comutator as comutator
import expression.evaluator_old as oldEvaluator
import expression.speedtest as speedtest
import utils.generator as generator

# шось графвіз тупенький якийсь
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'


if __name__ == "__main__":
    """ Lab 1 (required) """
    # expression = Corrector(generator.genRandomEquation(100)).correct()
    expression = Corrector("a*(b+(c+d)/e)+b*0+5+4-1*n").correct()
    # expression = generator.genRandomEqationWithValues(10, 9)

    """ Lab 3 """
    # expression = associator.associate(expression)

    """ Lab 4 """
    # expressions = comutator.comutate(expression, False)

    """ Lab 2 """
    # expTree = tree.parseExpression(expression)
    # expTree.printPrefix()
    # graph = expTree.generateGraph()
    # graph.render(filename='graph.dot', directory='generated_graphs', view=True, format='png') 

    """ Lab 5 """
    # params = {
    #     "a": 1,
    #     "b": 2,
    #     "c": 3,
    #     "d": 4,
    #     "e": 5,
    #     "n": 6,
    # }
    # result = oldEvaluator.evaluate(expression, params)
    
    """ Lab 6 """
    speedtest.test(expression)

    # a*(a+b+c)-a*b+c*d+v*f
    # a*(b+(c+d)/e)+b*0+5+4-1*n
    # 0+b*0+0*a+a*b+1
    # 2+3+4+5+6+7+8*s-p
    # -a+(v+p*(6-h+b*(d+u+5+10)))