class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        s1Counter = Counter(s1)

        s2Counter = {}
        l = 0
        for r in range(len(s2)):
            s2Counter[s2[r]] = s2Counter.get(s2[r],0) + 1

            if r + 1 -l > len(s1):
                s2Counter[s2[l]] -= 1
                
                if s2Counter[s2[l]] == 0:
                    del s2Counter[s2[l]] 
                l += 1


            if s2Counter == s1Counter:
                return True

        return False
