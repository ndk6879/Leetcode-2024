class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        l = 0
        cur = ''
        ans = 0

        for r in range(len(s)):
            cur += s[r]
            hashMap[s[r]] = hashMap.get(s[r],0) + 1

            while (r + 1 - l) - max(hashMap.values()) > k:
                hashMap[s[l]] -= 1
                l += 1
            ans = max(ans, r + 1 - l)
        return ans
