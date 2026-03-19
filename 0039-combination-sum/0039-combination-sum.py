'''
현재 숫자를 쓴다
현재 숫자를 안 쓰고 다음 숫자로 간다
'''
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