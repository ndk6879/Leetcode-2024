class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subSet = []

        def dfs(i):

            if sum(subSet.copy()) == target:
                res.append(subSet.copy())
                return

            
            if i >= len(candidates) or sum(subSet.copy()) > target:
                return
            
            subSet.append(candidates[i])
            dfs(i)
            subSet.pop()
            dfs(i+1)


        dfs(0)
        return res