class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s 
        ans = ''
        
        for r in range(numRows):
            interval = 2*(numRows-1) #0 4 , 1/5
            for i in range(r,len(s), interval):
                ans += s[i]
                if (r > 0 and r < numRows -1 and 
                (i + interval - 2*r) < len(s)):
                    ans += s[i + interval - 2*r]

        return ans