class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        ans = 0
        ansLen = ''
        for i in range(len(s)):

            #odd
            l, r = i,i

            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if len(ansLen) < (r + 1 - l):
                    ans = max(ans, r + 1 - l)
                    ansLen = s[l:r+1]

                l -= 1
                r +=1
            

            #even
            l, r = i, i+1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if len(ansLen) < (r + 1 - l):
                    ans = max(ans, r + 1 - l)
                    ansLen = s[l:r+1]

                l -= 1
                r +=1
        return ansLen