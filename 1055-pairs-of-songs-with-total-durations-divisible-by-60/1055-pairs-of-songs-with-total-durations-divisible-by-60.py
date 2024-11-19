class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = [0] * 60
        ans = 0
        print('t:',100 % 60)
        for t in time:
            complement = t % 60
            mod = (60 - complement) % 60
            ans += remainder[mod]
            remainder[complement] += 1
        return ans