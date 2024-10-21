class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        ans = 0
        for num in nums:
            tmp = 1
            cur = num
            if (num-1) not in numSet:
                while (cur+1) in numSet:
                    tmp += 1
                    cur += 1
            ans = max(ans,tmp)
        return ans