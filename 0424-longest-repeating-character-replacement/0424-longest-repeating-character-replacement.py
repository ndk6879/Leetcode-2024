class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        l = 0 
        ans = 0

        for r in range(len(s)):
            if s[r] not in hashMap:
                hashMap[s[r]] = 1

            else:
                hashMap[s[r]] += 1

            while (r + 1 - l - max(hashMap.values())) > k:
                hashMap[s[l]] -= 1
                l += 1

            ans = max(ans, r + 1 - l)
        return ans