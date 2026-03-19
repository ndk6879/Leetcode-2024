class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        subSet = []

        def dfs(i):
            if sum(subSet[:]) == target:
                ans.append(subSet[:])
                return
            
            if i >= len(candidates) or sum(subSet[:]) > target:
                return
            

            subSet.append(candidates[i])
            dfs(i)
            subSet.pop()
            dfs(i+1)

        dfs(0)
        return ans