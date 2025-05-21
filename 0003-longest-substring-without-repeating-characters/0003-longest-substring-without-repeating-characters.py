class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        l = 0
        hashMap = {}

        for r in range(len(s)):
            if s[r] in hashMap:
                print('s[r]',s[r],l)
                l = max(l, hashMap[s[r]]+1)
                print('s[r]',s[r],l,'\n')
            print(r,s[l:r+1])

            hashMap[s[r]] = r
            ans = max(ans, r+1-l)

        return ans
        