class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        print('ans:',ans)
        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix = postfix * nums[i+1]
            ans[i] = ans[i] * postfix
        return ans