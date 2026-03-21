class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        l,r
        r < len(prices):
            r += 1
        
        if prices[l] > prices[r]: move l
        '''

        l,r = 0,0
        ans = 0

        while (r < len(prices)):
            total = prices[r] - prices[l]
            if total < 0:
                l += 1
                r = l
             
            ans = max(ans,total)
            r += 1
        return ans