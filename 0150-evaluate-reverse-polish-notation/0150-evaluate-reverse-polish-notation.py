class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(int(token))

            elif token[0] == '-' and len(token) > 1:
                stack.append(int(token))

                
            elif token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(float(num2) / num1))
            # print('stack:',stack)
            
        return stack[-1]

