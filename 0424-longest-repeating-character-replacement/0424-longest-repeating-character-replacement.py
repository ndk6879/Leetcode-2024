class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0,0
        adict = {}
        ans = 0

        while (r < len(s)):
            adict[s[r]] = adict.get(s[r],0) + 1

            while ((r + 1 - l) - max(adict.values()) > k):
                adict[s[l]] -= 1
                l +=1

            ans = max(ans, 1 + r - l)
            r += 1

        return ans