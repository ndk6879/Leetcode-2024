class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {']':'[','}':'{',')':'('}
        openingList = ['[','(','{']
        for i in s:
            if i in openingList:
                stack.append(i)
            else:
                if stack == [] or not opening[i] == stack.pop(): return False

        return stack == []