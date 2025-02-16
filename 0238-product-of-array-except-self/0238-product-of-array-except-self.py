class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix = prefix * nums[i-1]
            ans[i] = ans[i] * prefix
        
        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix = postfix * nums[i+1]
            ans[i] = ans[i] * postfix

        return ans