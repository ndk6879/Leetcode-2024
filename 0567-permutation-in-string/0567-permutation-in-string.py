from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0 ,0
        hashS1 = Counter(s1)
        hashS2 = {}


        while (r < len(s2)):

            if (r + 1 - l) >= len(s1):
                if hashS1 == Counter(s2[l:r+1]):
                    return True
                l += 1
                continue
            r += 1
        return False