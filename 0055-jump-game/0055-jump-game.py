class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cur = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= cur:
                cur = i

        return cur == 0
        