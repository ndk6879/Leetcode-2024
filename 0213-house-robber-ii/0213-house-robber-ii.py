class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        
        return max(self.maxRob(nums[:-1]),self.maxRob(nums[1:]))

    
    def maxRob(self,nums):

        arr = [0 for _ in range(len(nums))]
        arr[0] = nums[0]
        arr[1] = max(nums[1],nums[0])

        for i in range(2,len(nums)):
            arr[i] = max(nums[i] + arr[i-2], arr[i-1])

        return max(arr)