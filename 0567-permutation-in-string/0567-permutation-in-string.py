from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Counter = Counter(s1)
        s2Counter = {}

        l = 0

        for r in range(len(s2)):
            s2Counter[s2[r]] = 1 + s2Counter.get(s2[r],0)

            if (r + 1 - l) > len(s1):
                s2Counter[s2[l]] -= 1
                
                if s2Counter[s2[l]] == 0:
                    del s2Counter[s2[l]]

                l += 1


            
            if s1Counter == s2Counter: return True

        return False