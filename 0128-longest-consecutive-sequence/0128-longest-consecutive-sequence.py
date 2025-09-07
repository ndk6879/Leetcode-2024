class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        ans = 0
        for num in numSet:
            if (num - 1) not in numSet:

                j = 1
                while (num + j) in numSet:
                    j += 1

                ans = max(ans,j)

        return ans