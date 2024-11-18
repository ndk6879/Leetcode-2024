class Solution:
    def longestPalindrome(self, s: str) -> str:
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