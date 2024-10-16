class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        '''
        1. get all combinations of times
        2. check if divisible by 60

        or 
        two pointer, binart search, sliding window
        '''
        
        remainder = 60 * [0]
        ans = 0

        for t in time:
            mod = t % 60
            complement = (60 - mod) % 60
            
            ans += remainder[complement]
            remainder[mod] += 1
        return ans