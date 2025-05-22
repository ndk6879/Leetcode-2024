class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax , curMin = 1, 1
        ans = 0

        for num in nums:
            tmp = curMax * num
            curMax = max(num, curMax * num, num * curMin )
            curMin = min(num, tmp, num * curMin)
            ans = max(ans,curMax)

        return ans