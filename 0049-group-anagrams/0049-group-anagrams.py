from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        for string in strs:
            tmp = [0] * 26
            for s in string:
                tmp[ord(s) - ord('a')] += 1

            if tuple(tmp) not in ans:
                ans[tuple(tmp)] = [string]

            else:
                ans[tuple(tmp)].append(string)
        
        return list(ans.values())