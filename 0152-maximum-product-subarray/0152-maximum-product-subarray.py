class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[-1]
        arr = [1] * len(nums)
        valMax = 0
        valMin = 0
        ans = 0
        for num in nums:
            tmp = valMax
            valMax = max(num, valMax * num, valMin*num)
            valMin = min(num, valMin * num, tmp*num)
            ans = max(ans,valMax)
        return ans
