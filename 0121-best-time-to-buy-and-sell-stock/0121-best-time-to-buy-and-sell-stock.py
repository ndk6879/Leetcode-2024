class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        ans = 0

        for r in range(len(prices)):
            total = prices[r] - prices[l]

            if total < 0:
                l = r
                continue

            ans = max(ans, total)

        return ans