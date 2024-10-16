class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        #1. starting element. n - 1 DNE
        #2. count it
        '''
        ans = 0
        numSet = set(nums)
        for num in nums:
            tmp = 1
            if num - 1 not in numSet:
                cur = num
                while cur +1 in numSet:
                    tmp += 1
                    cur += 1
            ans = max(ans, tmp)
        return ans