class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cur = ''
        l = 0
        hashMap = {}

        for r in range(len(s)):
            hashMap[s[r]] = r
            if s[r] in cur:
                l = max(l , hashMap[s[r]] + 1)
            ans = max(ans, r + 1 - l)
            cur += s[r]        

        return ans