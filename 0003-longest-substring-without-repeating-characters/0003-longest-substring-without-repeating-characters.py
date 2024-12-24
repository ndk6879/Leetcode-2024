class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        ans = 0
        l = 0
        cur = ''

        for r in range(len(s)):
            if s[r] in cur:
                l = max(hashMap[s[r]]+1, l)
                
            cur += s[r]
            ans = max(ans, r + 1 -l)
            hashMap[s[r]] = r
        return ans