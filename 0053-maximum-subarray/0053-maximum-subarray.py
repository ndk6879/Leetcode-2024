class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = [0] * len(nums)
        ans[0] = nums[0]

        for i in range(1,len(nums)):
            ans[i] = max(nums[i],nums[i] + ans[i-1])
        
        print('ans:',ans)
        return max(ans)