import expression.associator as associator
import expression.comutator as comutator
import expression.evaluator as evaluator
import expression.tree as tree


def test(baseExp:str):
    results = {}
    processes = 6
    
    # # graph rendering snippet
    # t.generateGraph()
    # graph = t.generateGraph()
    # graph.render(filename='graph.dot', directory='generated_graphs', view=True, format='png') 
    
    # base single
    t = tree.parseExpression(baseExp)
    results["base_1"] = {}
    results["base_1"]["exp"] = baseExp
    results["base_1"]["speed"] = evaluator.evaluate(t, 1, True)
    # base parallel
    t = tree.parseExpression(baseExp)
    results[f"base_{processes}"] = {}
    results[f"base_{processes}"]["exp"] = baseExp
    results[f"base_{processes}"]["speed"] = evaluator.evaluate(t, processes, True)
    
    # associated single
    t = tree.parseExpression(associator.associate(baseExp))
    results[f"ass_1"] = {}
    results[f"ass_1"]["exp"] = baseExp
    results[f"ass_1"]["speed"] = evaluator.evaluate(t, 1, True)
    
    # associated parallel
    t = tree.parseExpression(associator.associate(baseExp))
    results[f"ass_{processes}"] = {}
    results[f"ass_{processes}"]["exp"] = baseExp
    results[f"ass_{processes}"]["speed"] = evaluator.evaluate(t, processes, True)
    
    # 5 commutated single
    for _ in range(1, 4):
        t = tree.parseExpression(next(comutator.comutate(baseExp)))
        results[f"com_1"] = {"exp": [], "speed":[]}
        results[f"com_1"]["exp"].append(baseExp)
        results[f"com_1"]["speed"].append(evaluator.evaluate(t, 1, True))
    
    # 5 commutated single
    for _ in range(1, 4):
        t = tree.parseExpression(next(comutator.comutate(baseExp)))
        results[f"com_{processes}"] = {"exp": [], "speed":[]}
        results[f"com_{processes}"]["exp"].append(baseExp)
        results[f"com_{processes}"]["speed"].append(evaluator.evaluate(t, processes, True))