class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        l, r = 0, 1
        while(r < len(prices)):
            profit = prices[r] - prices[l]
            print('profit:',profit)
            if profit < 0:
                l = r
                continue
            ans = max(ans, profit)
            r += 1
        return ans
