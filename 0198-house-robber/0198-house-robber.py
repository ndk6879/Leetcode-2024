class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)

        ans = [0 for _ in range(len(nums))]

        ans[0] = nums[0]
        ans[1] = max(nums[0] , nums[1])

        for i in range(2,len(nums)):
            ans[i] = max( nums[i] + ans[i-2],ans[i-1] )
        return ans[-1]