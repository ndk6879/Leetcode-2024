class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        ans = 0 

        for r in range(len(prices)):
            profit = prices[r] - prices[l]

            if profit < 0:
                l = r
                continue

            ans = max(ans, profit)
        return ans