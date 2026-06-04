class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l,r = 0,0
        subSet = set()
        ans = 0
        while (r < len(s)):
            while s[r] in subSet:
                subSet.remove(s[l])
                l += 1

            subSet.add(s[r])
            ans = max(ans, r + 1 - l)
            r += 1
        return ans