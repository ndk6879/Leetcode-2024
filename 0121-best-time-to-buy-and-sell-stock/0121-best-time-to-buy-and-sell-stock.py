class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0,1

        '''
        if price[l] > price[r]: move l += 1
        ow r += 1

        '''
        ans = 0

        while (r < len(prices)):
            total = prices[r] - prices[l]

            if total < 0:
                l += 1
                r = l + 1
            
            else:
                r += 1
            
            ans = max(total,ans)
    
        return ans