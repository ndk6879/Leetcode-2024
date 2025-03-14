class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        
        for i in range(len(s)):

            l,r = i,i

            while(l >= 0 and r < len(s) and s[l]==s[r]):
                if (res < r + 1 - l):
                    
                    string = s[l:r+1]
                    res = max(res, r + 1 - l)
                l -= 1
                r += 1

            l,r = i,i+1

            while(l >= 0 and r < len(s) and s[l]==s[r]):
                if (res < r + 1 - l):
                    
                    string = s[l:r+1]
                    res = max(res, r + 1 - l)
                l -= 1
                r += 1

            
        return string