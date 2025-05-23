class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr = [0] * len(nums)

        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    arr[i] = max(arr[j]+1, arr[i])

        return max(arr) + 1