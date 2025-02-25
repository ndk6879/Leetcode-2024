class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        cur = []

        def dfs(i, total):
            if total == target:
                if cur.copy() not in ans:
                    ans.append(cur.copy())
                    return

            elif i >= len(candidates) or total > target:
                return False

            cur.append(candidates[i])
            
            dfs(i+1, total + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)


        dfs(0, 0)

        return ans