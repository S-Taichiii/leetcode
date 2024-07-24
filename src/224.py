from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        if s.isdecimal(): return int(s)

        val_stack = deque()
        ope_stack = deque()
        operators = ["+", "-", "(", ")"]
        num_str = ""

        s = "(" + s + ")"
        for token in s:
            if token == " ": continue
            elif token not in operators:
               num_str += token 
            else:
                if token == "(":
                    ope_stack.append(token)
                elif token == ")":
                    if num_str != "":
                        val_stack.append(int(num_str))
                        num_str = ""
                    operator = ope_stack.pop()

                    while operator != "(":
                        num1 = val_stack.pop()
                        num2 = val_stack.pop()
                        val_stack.append(self.eval(num1, num2, operator))
                        operator = ope_stack.pop()
                else:
                    if len(val_stack) != 0 and len(ope_stack) != 0 and ope_stack[-1] != "(" and ope_stack[-1] != ")" and num_str != "":
                        val_stack.append(self.eval(int(num_str), val_stack.pop(), ope_stack.pop()))
                        num_str = ""
                        ope_stack.append(token)
                    else:
                        ope_stack.append(token)
                        if num_str != "":
                            val_stack.append(int(num_str))
                            num_str = ""
            
        return val_stack[0]
        
    def eval(self, num1: int, num2: int, operator: str) -> int:
        result = 0
        match operator:
            case "+":
                result = num2 + num1
            case "-":
                result = num2 - num1

        return result

solution = Solution()
print(solution.calculate(" 1 + 1"))
print(solution.calculate(" 2-1 + 2"))
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))
print(solution.calculate("1234"))
print(solution.calculate("1 - (   -2)"))
