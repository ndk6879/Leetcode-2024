class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        ans = 0
        hashMap = {}
        curSet = set()

        for r in range(len(s)):
            while s[r] in curSet:
                curSet.remove(s[l])
                l += 1
                
            hashMap[s[r]] = r
            curSet.add(s[r])
            ans = max(ans,r + 1 - l)

        return ans