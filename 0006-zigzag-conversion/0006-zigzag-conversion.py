class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        if numRows == 1: return s
        for i in range(numRows):
            intervals = (numRows - 1)*2
            for j in range(i,len(s), intervals):
                ans += s[j]

                if (i > 0 and i < (numRows - 1) and (j + intervals - 2*i) < len(s)):
                    ans += s[j + intervals - 2*i]
        return ans