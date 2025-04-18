class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            l, r = i,i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                ans += 1
            
            l, r = i, i+1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                ans += 1
        return ans