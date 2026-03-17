#each time, in decision tree, we can make 2 decisions and elment can be 1. So, time complexity = 2^t where t = target
#그리고 backtracking을 함으로써, [2,2,3]을 먼저 찾아서 [3,2,2] 같은 일이 발생하지 않음
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subSet = []

        def dfs(i):

            if sum(subSet.copy()) == target:
                res.append(subSet.copy())
                return

            
            if i >= len(candidates) or sum(subSet.copy()) > target:
                return
            
            subSet.append(candidates[i])
            dfs(i)
            subSet.pop()
            dfs(i+1)


        dfs(0)
        return res