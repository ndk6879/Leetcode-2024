class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMax, curMin = 1,1
        for num in nums:
            tmp = curMax*num
            curMax = max(num, curMax*num,curMin*num)
            curMin = min(num, tmp,curMin*num)
            ans = max(ans, curMax)
        return ans