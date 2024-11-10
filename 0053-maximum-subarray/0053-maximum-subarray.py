class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        arr = [0 for _ in range(len(nums))]
        arr[0] = nums[0]
        ans = arr[0]
        for i in range(1,len(nums)):
            arr[i] = max(nums[i], nums[i]+arr[i-1])
            ans = max(ans,arr[i])
        return ans