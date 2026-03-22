class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l + 1
        ans = 0

        while(r < len(prices)):

            total = prices[r] - prices[l]
            if total < 0:
                l += 1
            else:
                
                ans = max(ans, total)
                r += 1
        return ans