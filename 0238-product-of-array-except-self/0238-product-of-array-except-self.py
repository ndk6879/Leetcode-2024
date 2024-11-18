class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1 for _ in range(len(nums))]
        
        prefix = 1
        for i in range(len(nums)):
            arr[i] = prefix
            prefix = prefix * nums[i]

        print('arr:',arr)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= postfix
            postfix = postfix * nums[i]
        print('arr:',arr)
        return arr