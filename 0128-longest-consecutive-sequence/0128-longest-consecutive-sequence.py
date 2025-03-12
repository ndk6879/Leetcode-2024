class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        numsSet = set(nums)

        ans = 0
        for num in numsSet:
            if (num-1) not in numsSet:
                length = 1
                while num+length in numsSet:
                    length += 1

                ans = max(ans, length)
        return ans
