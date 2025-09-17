class Solution:
    def isPalindrome(self, s: str) -> bool:

        tmp = ''
        
        for c in s:
            if c.isalnum():
                tmp += c.lower()

        return tmp == tmp[::-1]