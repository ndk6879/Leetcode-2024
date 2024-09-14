class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        ans = 0
        lowest = float("inf")

        for l in range(len(prices)):
            i = l + 1
            if prices[l] == prices[l-1] and l < len(prices):
                continue

            while (i<len(prices)):
                total = prices[i] - prices[l]
                if total < 0:
                    i += 1
                    continue
                
                elif total >= 0:
                    ans = max(ans, total)
                    i += 1
                    while (i < len(prices) and prices[i] == prices[i-1]):
                        i += 1
        return ans
            
        