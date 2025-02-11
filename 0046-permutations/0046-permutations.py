class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def dfs(arr):
            
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            
            
            for i in range(len(arr)):
                if not arr[i]:
                    arr[i] = True
                    subset.append(nums[i])
                    dfs(arr)
                    subset.pop()
                    dfs(arr)
                    arr[i] = False
        
        dfs([False]*len(nums))
        return res