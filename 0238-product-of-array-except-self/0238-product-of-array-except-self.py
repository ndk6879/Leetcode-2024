class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)

        prefix = 1
        for i in range(1,len(nums)):
            prefix = prefix * nums[i-1]
            ans[i] = ans[i] * prefix

        print('ans:',ans)
        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix = nums[i+1] * postfix
            ans[i] = ans[i] * postfix
        print('ans:',ans)
        return ans