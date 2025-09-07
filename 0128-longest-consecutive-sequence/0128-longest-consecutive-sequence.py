class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 1
        
        numSet = set(nums)

        ans = 0
        for num in nums:
            if (num - 1) not in numSet:
                tmp = 1

                j = 1
                while (num + j) in numSet:
                    tmp += 1
                    j += 1

                ans = max(ans,tmp)

        return ans