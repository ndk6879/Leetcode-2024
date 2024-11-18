class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        ans = 0
        while(r < len(prices)):
            profit = prices[r] - prices[l]

            if profit <= 0:
                l += 1
                r = l + 1
                continue
            
            ans = max(ans, profit)
            r += 1
        return ans