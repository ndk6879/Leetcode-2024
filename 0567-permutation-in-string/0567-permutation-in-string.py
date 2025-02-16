from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)
        l = 0

        curS2 = {}
        for r in range(len(s2)):
            curS2[s2[r]] = 1 + curS2.get(s2[r],0)

            if r + 1 - l > len(s1):
                curS2[s2[l]] -= 1

                if curS2[s2[l]] == 0:
                    del curS2[s2[l]]
                l += 1

            if curS2 == s1Counter:
                return True

            
            
            
        return False