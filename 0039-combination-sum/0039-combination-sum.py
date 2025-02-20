class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        cur = []
        ans = []

        def dfs(i):
            if sum(cur) == target:
                ans.append(cur.copy())
                return

            elif sum(cur) > target or i >= len(candidates):
                return False

            cur.append(candidates[i])
            dfs(i)

            cur.pop()
            dfs(i+1)

        dfs(0)

        return ans