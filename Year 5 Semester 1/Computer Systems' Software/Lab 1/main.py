from expression import Expression
from generator import genRandomEquation

Expression(genRandomEquation(100)).correct()
# Expression("").correct()
# Expression("a-+(t*5.81.8 - ))/?").correct()