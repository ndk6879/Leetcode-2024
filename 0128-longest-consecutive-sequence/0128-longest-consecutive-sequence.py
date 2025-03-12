class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0

        sett = set(nums)
        for num in nums:
            if num - 1 not in sett:
                cur = num
                tmp = 0
                while cur in sett:
                    cur += 1
                    tmp += 1
                ans = max(ans,tmp)
        return ans