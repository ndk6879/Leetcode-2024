class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,0
        ans = 0
        hashMap = {}

        while (r < len(s)):

            if s[r] in hashMap:
                print(s[r])
                l = max(l,hashMap[s[r]]+1)
            
            hashMap[s[r]] = r
            ans = max(ans , r + 1 - l)
            r += 1
        
        return ans