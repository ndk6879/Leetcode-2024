class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        subSet = []

        def dfs(i):
            if i >= len(nums):
                ans.append(subSet[:])
                return
            
            subSet.append(nums[i])
            dfs(i+1)

            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            subSet.pop()
            dfs(i+1)

        dfs(0)
        return ans