class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = [0] * 60
        ans = 0
        for t in time:
            mod = t % 60
            complement = (60 - mod) % 60
            ans += remainder[complement]
            remainder[mod] += 1
        return ans