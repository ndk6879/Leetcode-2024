class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans = ans*26 + ord(columnTitle[i])+1 - ord('A')
        return ans