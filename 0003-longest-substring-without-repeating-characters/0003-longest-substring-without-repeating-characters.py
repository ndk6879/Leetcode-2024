class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        ans = 0
        cur = ''
        hashMap = {}
        for r in range(len(s)):
            if s[r] in cur:
                l = max(hashMap[s[r]] + 1, l)
            
            hashMap[s[r]] = r

            cur += s[r]
            ans = max(ans,r + 1 - l)

        return ans