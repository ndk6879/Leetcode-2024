class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            # print('token:',token,stack)
            
            if token.isdigit() or len(token) > 1 and token[0] == '-':
                stack.append(token)

            elif token == '+':
                cur1 = int(stack.pop())
                cur2 = int(stack.pop())
                stack.append(cur1+cur2)

            elif token == '-':
                cur1 = int(stack.pop())
                cur2 = int(stack.pop())
                stack.append(cur2 - cur1)

            elif token == '*':
                cur1 = int(stack.pop())
                cur2 = int(stack.pop())
                stack.append(cur1 * cur2)

            elif token == '/':
                cur1 = int(stack.pop())
                cur2 = int(stack.pop())
                stack.append(cur2 / cur1)
            

        return int(stack[-1])

            