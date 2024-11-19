class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        
        if numRows == 1: return s
        
        for r in range(numRows):
            intervals = (numRows - 1) * 2
            for i in range(r,len(s),intervals):
                ans += s[i]
                if (0 < r and r < (numRows)-1 and (i+intervals-2*r) < len(s)):
                    ans += s[i+intervals-2*r]
        return ans