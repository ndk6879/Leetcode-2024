class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        arr[0] = nums[0]

        for i in range(1,len(nums)):
            arr[i] = max(nums[i],arr[i-1]+nums[i])
        print('arr:',arr)
        return max(arr)