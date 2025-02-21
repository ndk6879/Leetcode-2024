class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print('candidates:',candidates)
        ans = []
        cur = []

        def dfs(i):
            if sum(cur) == target:
                if cur not in ans:
                    ans.append(cur.copy())
                    return
                           

            if i >= len(candidates) or sum(cur) > target: 
                return False

            cur.append(candidates[i])
            
            dfs(i+1)
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1)
            

        dfs(0)
        return ans