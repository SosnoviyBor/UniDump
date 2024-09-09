import Coloring

class Expression:
    expressionSymbols = "+-*/^"
    
    currentlyDecimal = False
    currentlyFunction = False
    openBrackets = 0
    
    i = 0
    realIndex = 2
    mishapIndexes = []
    
    
    def __init__(self, expression:str) -> None:
        normalizedExpression = expression.replace(" ", "")
        self.initExpression = normalizedExpression
        self.expression = [symbol for symbol in normalizedExpression]
    
    
    def correct(self) -> None:
        currentSymbol = None
        nextSymbol = None
        currentUnmodifiedExpressionView = list.copy(self.expression)
        
        print(
            "##### Початковий вираз #####\n" +
            f"{Coloring.wrap(self.initExpression, Coloring.Color.Foreground.CYAN)}\n" +
            "-------------------------\n" +
            "##### Основна перевірка #####"
        )
        
        # не дерево розгалуджень, а цілий бляха ліс
        self.i = 0
        while self.i < len(self.expression)-1:
            currentSymbol:str = self.expression[self.i]
            nextSymbol:str = self.expression[self.i+1]
            
            # початок виразу
            if self.i == 0 and not (currentSymbol.isalnum() or currentSymbol in "-("):
                self.realIndex -= 1
                self.mishap(f"Вираз почався з {currentSymbol}, а не числа чи змінної", True)
                self.mishapIndexes[self.i + self.realIndex - 1] += 1
                self.realIndex += 1
                # цей блок - один суцільний костиль
                # хоча все інше не сильно краще ;-;
            
            elif currentSymbol.isdigit():
                if self.currentlyDecimal and nextSymbol == ".":
                    self.mishap("Зайва крапка десяткового дробу", False)
                elif self.currentlyFunction and nextSymbol == ".":
                    self.mishap(f"Крапка в назві функції", False)
                elif nextSymbol == ".":
                    self.currentlyDecimal = True
                elif nextSymbol.isalpha() and not self.currentlyFunction:
                    self.mishap(f"Константа може складатись лише з цифр", False)
            
            elif currentSymbol.isalpha():
                self.currentlyFunction = True
                if nextSymbol == ".":
                    self.mishap(f"Крапка в назві функції", False)
            
            elif currentSymbol in self.expressionSymbols:
                self.currentlyDecimal = False
                self.currentlyFunction = False
                if nextSymbol in self.expressionSymbols:
                    self.mishap(f"Оператор '{nextSymbol}' після іншого оператора", False)
                elif nextSymbol == ")":
                    self.mishap("Вираз у дужці не може закінчуватись оператором", True)
                elif nextSymbol == ".":
                    self.mishap("Крапка десяткового дробу після оператора", False)
            
            elif currentSymbol == "(":
                self.openBrackets += 1
                self.currentlyDecimal = False
                self.currentlyFunction = False
                if not (nextSymbol.isalnum() or nextSymbol == "-"):
                    self.mishap("Вираз у дужці повинен починатись із числа чи змінної", False)
            
            elif currentSymbol == ")":
                if self.openBrackets == 0:
                    self.mishap("Зайва закриваюча дужка", True)
                    if self.expression[:self.i].count("(") > self.expression[:self.i].count(")"):
                        self.openBrackets += 1
                        self.i -= 1
                else:
                    if nextSymbol.isalnum() or nextSymbol in "(.":
                        self.mishap("Після дужки очікується оператор", False)
                    else:
                        # денкремент повинен бути доданий до кожного mishap(str, TRUE)
                        self.openBrackets -= 1
            
            elif currentSymbol == ".":
                if nextSymbol.isalpha():
                    self.mishap("Десятковий дріб не може містити змінних", False)
                elif nextSymbol in self.expressionSymbols + "()":
                    self.currentlyDecimal = False
                    self.mishap("Десятковий дріб не має жодних десяткових розрядів", True)
            
            else:
                self.mishap(f"Невідомий символ {nextSymbol}", True)
            
            self.i += 1
        
        # Перевірка кінця виразу
        while True:
            if not (self.expression[-1].isalnum() or self.expression[-1] == ")"):
                print(f"Позиція {self.i + self.realIndex} | Вираз закінчився '{self.expression[-1]}', а не числом чи змінною")
            elif self.expression[-1].isalnum() and self.expression[-2] == ")":
                print(f"Позиція {self.i + self.realIndex} | Після дужки очікується оператор")
            elif self.expression[-1] == ")" and self.expression.count(")") > self.expression.count("("):
                print(f"Позиція {self.i + self.realIndex} | Зайва закриваюча дужка")
            else:
                break
            # black magic index fuckery
            self.mishapIndexes.append(self.i + self.realIndex - 2)
            del self.expression[-1]
            self.realIndex += 1
        
        print(
            "##### Результат основної перевірки #####\n" +
            f"До:    {''.join(self.createHighlightedExpression(currentUnmodifiedExpressionView))}\n" +
            f"Після: {''.join(self.expression)}"
        )
        
        # Перевірка незакритих дужок
        if self.openBrackets > 0:
            print(
                "-------------------------\n" +
                "##### Перевірка на незакриті дужки #####"
            )
            self.mishapIndexes.clear()
            currentUnmodifiedExpressionView = list.copy(self.expression)
            
            indexOffset = 0
            unclosedBracketIndexes = []
            for i in range(len(self.expression)):
                if self.expression[i] == "(":
                    unclosedBracketIndexes.append(i)
                elif self.expression[i] == ")":
                    del unclosedBracketIndexes[:1]
            for i in unclosedBracketIndexes:
                self.mishapIndexes.append(i)
                print(f"Позиція {i + 1} | Незакрита дужка")
                del self.expression[i - indexOffset]
                indexOffset += 1
        
            print(
                "##### Результат перевірки на незакриті дужки #####\n" +
                f"До:    {''.join(self.createHighlightedExpression(currentUnmodifiedExpressionView))}\n" +
                f"Після: {''.join(self.expression)}"
            )
        
        # Виведення та повернення результатів
        if ''.join(self.expression) == self.initExpression:
            msg = f"{Coloring.wrap('Вираз коректний!', Coloring.Color.Foreground.GREEN)}"
        else:
            msg = ("##### Кінцевий результат #####\n" +
                f"{Coloring.wrap(''.join(self.expression), Coloring.Color.Foreground.GREEN)}")
        print("-------------------------\n" +
              msg)
        return ''.join(self.expression)
    
    
    def mishap(self, msg:str, currentSymbol:bool):
        if currentSymbol:
            j = self.i
        else:
            j = self.i + 1
        print(f"Позиція {j + self.realIndex - 1} | {msg}")
        self.mishapIndexes.append(j + self.realIndex - 2)
        del self.expression[j]
        
            
        self.i -= 1
        self.realIndex += 1
    
    def createHighlightedExpression(self, expression):
        arr = []
        for i in range(len(expression)):
            if i in self.mishapIndexes:
                arr.append(Coloring.wrap(expression[i], Coloring.Color.Foreground.RED))
            else:
                arr.append(expression[i])
        return arr