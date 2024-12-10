class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adict = {}
        

        for string in strs:
            tmp = [0] * 26
            for s in string:
                tmp[(ord(s) - ord('a'))] += 1
            
            if tuple(tmp) not in adict:
                adict[tuple(tmp)] = [string]
            else:
                adict[tuple(tmp)].append(string)
        
        ans = []
        for i in adict.values():
            ans.append(i)
        return ans