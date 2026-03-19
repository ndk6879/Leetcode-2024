class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates.sort()
        ans = []
        subSet = []

        def dfs(i):
            if sum(subSet[:]) == target:
                ans.append(subSet[:])
                return

            if i >= len(candidates) or sum(subSet[:]) > target:
                return
            
            subSet.append(candidates[i])
            dfs(i+1)
            subSet.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return ans