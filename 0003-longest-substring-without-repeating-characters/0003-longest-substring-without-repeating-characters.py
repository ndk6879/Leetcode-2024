class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        charSet = set()
        
        #abab
        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            ans = max(ans, r + 1 - l)
            charSet.add(s[r])

        return ans