import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value_stack: list[int] = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                num1 = value_stack.pop(-1)
                num2 = value_stack.pop(-1)
                result = self.eval(num1, num2, token)
                value_stack.append(result)
            else:
                value_stack.append(int(token))

        return value_stack[0]


    def eval(self, num1: int, num2: int, operator: str) -> int:
        result = 0
        match operator:
            case "+":
                result = num2 + num1
            case "-":
                result = num2 - num1
            case "*":
                result = num2 * num1
            case "/":
                result = math.ceil( num2 / num1 ) if num2 * num1 < 0 else math.floor(num2 / num1)

        return result

# 66ms
# Beats53.67%
# 17.14MB
# Beats15.17%

solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))
print(solution.evalRPN(["4","13","5","/","+"]))
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


