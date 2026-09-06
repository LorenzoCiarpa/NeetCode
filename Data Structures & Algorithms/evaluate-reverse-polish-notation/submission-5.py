class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for i, elem in enumerate(tokens):
            if elem in operations:
                num_1 = stack.pop()
                num_2 = stack.pop()

                if elem == "+":
                    result =  num_2 + num_1
                elif elem == "-":
                    result = num_2 - num_1
                elif elem == "*":
                    result = num_2 * num_1
                elif elem == "/":
                    result = num_2 / num_1
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                
                stack.append(result)
            else:
                stack.append(int(elem))
        return stack[-1]
