from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        hashMap = {}

        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r],0) + 1
            while(( (r+1-l) - max(hashMap.values()) > k )):
                hashMap[s[l]] -= 1
                l += 1

            ans = max(ans, r + 1 - l)
            print(r,ans)

        return ans