class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            arr[i] = max(arr[i-2] + nums[i] , arr[i-1])
        
    
        return arr[-1]