class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for string in strs:
            countArr = [0] * 26

            for s in string:
                countArr[ord(s) - ord('a')] += 1

            if tuple(countArr) not in ans:
                ans[tuple(countArr)] = [string]
            
            else:
                ans[tuple(countArr)].append(string)

        result = []
        for i in ans.values():
            result.append(i)

        return result