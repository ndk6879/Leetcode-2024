class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr = [False] * len(nums)
        arr[0] = True

        cur = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):    
            if i + nums[i] >= cur:
                cur = i

        return cur == 0