class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        - r  + 1 always
        - if repeating exist, l += 1
        '''
        
        l,r = 0,0
        curSet = set()
        ans = 0

        while (r < len(s)):

            while s[r] in curSet:
                curSet.remove(s[l])
                l += 1

            curSet.add(s[r])
            ans = max(ans, r + 1 - l)
            r += 1
        
        return ans