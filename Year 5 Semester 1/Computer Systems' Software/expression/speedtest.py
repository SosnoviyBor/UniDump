import expression.associator as associator
import expression.comutator as comutator
import expression.evaluator as evaluator
import expression.tree as tree


def test(baseExp:str):
    results = {}
    processes = 6
    
    # base single
    t = tree.parseExpression(baseExp)
    results["base_1"]["exp"] = baseExp
    results["base_1"]["speed"] = evaluator.evaluate(t, 1)
    
    # base parallel
    
    # associated single
    
    # associated parallel
    
    # 5 commutated single
    
    # 5 commutated single
    