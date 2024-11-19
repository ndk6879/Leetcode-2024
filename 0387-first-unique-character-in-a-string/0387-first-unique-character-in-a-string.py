class Solution:
    def firstUniqChar(self, s: str) -> int:
        adict = {}
        for i in s:
            if i not in adict:
                adict[i] = 1
            else: 
                adict[i] += 1
        
        print('addict:',adict)
        for k in adict:
            if adict[k] == 1:
                return s.index(k)
        else: return -1
        