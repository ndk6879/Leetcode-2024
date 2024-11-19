from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictS, dictT = {}, {}

        for a,b in zip(s,t):
            if a in dictS:
                if dictS[a] != b: return False
            else: 
                dictS[a] = b

            if b in dictT:
                if dictT[b] != a: return False
            else: 
                dictT[b] = a
        return True

