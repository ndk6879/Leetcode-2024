class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        l = 0
        hashMap = {}
        cur = ''

        for r in range(len(s)):
            if s[r] in cur:
                l = max(l, hashMap[s[r]]+1)
            hashMap[s[r]] = r
            

            cur += s[r]

            ans = max(ans,r + 1 - l)

        return ans