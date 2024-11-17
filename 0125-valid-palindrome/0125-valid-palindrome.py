class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        
        for i in s:
            if i.isalpha():
                newS += i.lower()
            
            elif i.isdigit():
                newS += i
        print('newS:',newS)
        return newS == newS[::-1]