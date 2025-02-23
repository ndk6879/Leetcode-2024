class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hashMap = {}
        ans = 0

        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r],0)

            while ((r + 1 - l) - max(hashMap.values())) > k:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1


            ans = max(ans, r + 1 - l)

        return ans