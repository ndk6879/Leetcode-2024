class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0

        sett = set(nums)
        for num in nums:
            if num - 1 not in sett:
                i = 1
                cnt = 1
                while num+i in sett:
                    cnt += 1
                    i += 1
                ans = max(ans,cnt)
        return ans