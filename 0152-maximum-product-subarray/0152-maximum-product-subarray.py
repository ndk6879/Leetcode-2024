class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[-1]
        arr = [1] * len(nums)
        curMax = 0
        curMin = 0
        ans = 0

        for i in range(len(nums)):
            tmp = curMax * nums[i]
            curMax = max(nums[i], curMax * nums[i], curMin * nums[i])
            curMin = min(nums[i], tmp, curMin * nums[i])
            ans = max(ans,curMax,curMin)
        return ans