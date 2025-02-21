class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print('candidates:',candidates)
        ans = []
        cur = []

        def dfs(i, total):
            if total == target:
                if cur not in ans:
                    ans.append(cur.copy())
                    return
                           

            if i >= len(candidates) or total > target: 
                return False

            cur.append(candidates[i])
            
            dfs(i+1, candidates[i] + total)
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)
            

        dfs(0, 0)
        return ans