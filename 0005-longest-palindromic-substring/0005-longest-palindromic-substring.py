class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for loop에서 각각의 letter go through할때, each letter에서 outward로 체크하는거임. 이것만 기억하셈
        
        ans = ''
        ansLen = 0

        for i in range(len(s)):
            
            l,r = i, i 
            while(0 <= l and r < len(s) and s[l] == s[r]):
                if ansLen < (r+1-l):
                    ans = s[l:r+1]
                    ansLen = r + 1 - l
                l -= 1
                r += 1

            l, r = i, i + 1
                
            while(0 <= l and r < len(s) and s[l] == s[r]):
                if ansLen < (r+1-l):
                    ans = s[l:r+1]
                    ansLen = r + 1 - l
                l -= 1
                r += 1
        
        return ans