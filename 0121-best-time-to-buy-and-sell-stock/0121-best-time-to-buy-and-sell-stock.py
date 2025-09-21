class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l + 1
        ans = 0
        while (r < len(prices)):
            
            price = prices[r] - prices[l]
            if price < 0: 
                l += 1
                r = l + 1
                continue
            
            else:
                ans = max(ans, price)
            r += 1
        return ans