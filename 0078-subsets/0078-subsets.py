class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subSet = []

        def dfs(ind):
            if ind >= len(nums):
                ans.append(subSet.copy())
                return
            
            subSet.append(nums[ind])
            dfs(ind+1)
            subSet.pop()
            dfs(ind+1)

        dfs(0)
        return ans