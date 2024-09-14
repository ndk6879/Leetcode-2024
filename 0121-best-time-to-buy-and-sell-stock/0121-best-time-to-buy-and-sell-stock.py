class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ans = 0
        while(r < len(prices)):
            profit = prices[r] - prices[l]
            if profit >= 0:
                ans = max(ans, profit)
                r += 1
            elif profit < 0:
                l = r
                r = l + 1
        return ans
        