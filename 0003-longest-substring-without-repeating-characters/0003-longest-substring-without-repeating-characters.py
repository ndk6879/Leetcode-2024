class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashMap = {}
        ans = 0
        string = ''
        l = 0

        for r in range(len(s)):
            if s[r] in string:
                l = max(l, hashMap[s[r]]+1)
                 

            string += s[r]
            ans = max(ans, r + 1 - l)
            hashMap[s[r]] = r

        return ans
