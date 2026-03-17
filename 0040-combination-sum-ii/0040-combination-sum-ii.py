class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subSet = []
        def dfs(i):
            if sum(subSet.copy()) == target and subSet.copy() not in res:
                res.append((subSet.copy()))

            if i>= len(candidates) or sum(subSet.copy()) > target:
                return

            subSet.append(candidates[i])
            dfs(i+1)

            subSet.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+= 1
            dfs(i+1)

        dfs(0)
        return res