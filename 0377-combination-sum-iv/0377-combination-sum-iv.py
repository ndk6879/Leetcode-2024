class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # 합이 0인 경우 방법의 수는 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:  # num을 사용 가능할 때
                    dp[i] += dp[i - num]

        return dp[target]
