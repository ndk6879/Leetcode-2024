class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        s1Counter = Counter(s1)
        l = 0
        hashMap = {}

        for r in range(len(s2)):
            if s2[r] not in hashMap:
                hashMap[s2[r]] = 1
            else:
                hashMap[s2[r]] += 1

            while r + 1 - l > len(s1):
                hashMap[s2[l]] -= 1
                if hashMap[s2[l]] == 0:
                    del hashMap[s2[l]]
                l += 1

            if hashMap == s1Counter: return True
        return False
