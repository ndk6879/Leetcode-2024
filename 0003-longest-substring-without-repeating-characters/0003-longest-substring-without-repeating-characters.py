class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        ans = 0
        hashMap = {}

        for r in range(len(s)):
            if s[r] in hashMap:
                l = max(l, hashMap[s[r]]+1)


            hashMap[s[r]] =r
            ans = max(ans, r + 1 - l)
        
        return ans