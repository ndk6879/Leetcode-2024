class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in setNums:
                i = 1
                cnt = 1
                while (num+i in setNums):
                    i += 1
                    cnt += 1
                ans = max(ans,cnt)
        return ans