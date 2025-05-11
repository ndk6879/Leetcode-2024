class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr = [1] * len(nums)

        prefix = 1
        for i in range(1,len(nums)):
            prefix = prefix * nums[i-1]
            arr[i] = arr[i] * prefix

        print('arr:',arr)

        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix = postfix * nums[i+1]
            arr[i] = arr[i] * postfix
        
        return arr