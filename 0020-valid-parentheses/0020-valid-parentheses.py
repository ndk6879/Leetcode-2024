class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1: return False

        
        stack = []
        opening = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
          }

        for i in s:
            if i in opening:
                stack.append(i)

            else:
                if stack == []: return False

                cur = stack.pop()
                if opening[cur] != i: return False
        return stack == []