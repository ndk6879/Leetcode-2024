class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        cur = ''
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in cur:
                l = max(l, hashMap[s[r]] +1)

            
            cur += s[r]
            ans = max(ans, r + 1 - l)
            hashMap[s[r]] = r
        return ans