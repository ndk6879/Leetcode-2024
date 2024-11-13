class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening = {')':'(',
        '}':'{',
        ']':'['}
        
        for i in s:
            if i in opening.values():
                stack.append(i)

            else:
                if stack == []: return False
                if not opening[i] == stack.pop(): return False
                
        return stack == []
        