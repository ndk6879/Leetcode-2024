class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(ind, path):
            if sum(path) == target:
                ans.append(path[:])
                return

            if sum(path) > target or ind >= len(candidates): return 
            
            path.append(candidates[ind])
            dfs(ind,path)
            path.pop()

            dfs(ind+1,path)

        dfs(0,[])

        return ans