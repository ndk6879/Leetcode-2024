class Solution:
    def maxProfit(self, prices: List[int]) -> int:

            l = 0
            ans = 0
            r = l + 1
            while(r<len(prices)):
                profit = prices[r] - prices[l]
                if profit < 0:
                    l += 1
                    r = l + 1

                elif profit >= 0:
                    ans = max(ans,profit)
                    r += 1

            return ans