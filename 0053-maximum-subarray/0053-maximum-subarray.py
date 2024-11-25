class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        arr[0] = nums[0]
        ans = 1

        for i in range(1,len(nums)):
            arr[i] = max(nums[i], nums[i]+arr[i-1])
        print('arr:',arr)
        return max(arr)
        