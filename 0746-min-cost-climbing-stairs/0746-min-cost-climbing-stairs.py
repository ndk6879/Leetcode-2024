class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = 0, 0  # a = dp[i-2], b = dp[i-1]

        for c in cost:
            a, b = b, min(a, b) + c

        return min(a, b)
