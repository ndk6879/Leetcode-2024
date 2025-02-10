class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []

        def dfs(i):
            if sum(cur) == target:
                ans.append(cur.copy())
                return

            if i >= len(candidates) or sum(cur) > target or cur in ans:
                return

            cur.append(candidates[i])
            dfs(i)
            
            cur.pop()
            dfs(i+1)

        dfs(0)
        return ans