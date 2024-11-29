class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            
            arr = [0]*len(nums)
            arr[0] = nums[0]
            arr[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                arr[i] = max(arr[i-1], arr[i-2]+nums[i])
            return arr[-1]

        if len(nums) < 3:
            return max(nums)

        return max(helper(nums[1:]),helper(nums[:-1]))
        
    
        
