class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #1. create a dp array to store values at each index
        #2. compare nums[i] and nums[i] + dp[i-1]

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            dp[i] = max(nums[i],nums[i] + dp[i-1])
        return max(dp)