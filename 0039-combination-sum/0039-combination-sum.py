class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        ans = []

        def dfs(i, total):
            if total == target:
                ans.append(cur.copy())
                return

            elif total > target or i >= len(candidates):
                return False

            cur.append(candidates[i])
            dfs(i, total + candidates[i])

            cur.pop()
            dfs(i+1, total)

        dfs(0,0)

        return ans     