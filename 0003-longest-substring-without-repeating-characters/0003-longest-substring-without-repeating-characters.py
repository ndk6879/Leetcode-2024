class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        cur = ''
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in cur:
                l = max(hashMap[s[r]] + 1, l)
            
            cur += s[r]
            hashMap[s[r]] = r
            ans = max(ans, r + 1 - l)
        return ans