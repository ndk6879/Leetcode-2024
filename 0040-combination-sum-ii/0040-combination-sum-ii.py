class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = []

        def dfs(index, path):
            if sum(path) == target:
                ans.append(path[:])
                return

            if sum(path) > target or index >= len(candidates):
                return

            path.append(candidates[index])
            dfs(index+1, path)
            path.pop()
            while index+1 < len(candidates) and candidates[index]==candidates[index+1]:
                index += 1
            dfs(index+1,path)

        dfs(0,[])
        return ans