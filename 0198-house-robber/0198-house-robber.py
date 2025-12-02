class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        
        
        a = nums[0]
        b = max(nums[1],nums[0])

        for i in range(2,len(nums)):
            a,b = b, max(b,nums[i] + a)
        
        return b