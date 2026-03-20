class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        use two pointers l and r
        increment r by 1 
        increment l if repeating happens
        '''

        ans = 0
        l,r = 0,0
        curSet = set()
        while(r < len(s)):

            while s[r] in curSet:
                curSet.remove(s[l])
                l += 1

            curSet.add(s[r])
            r+=1
            ans = max(ans, r -l)
        return ans