class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1  
        ans = 0
        while (l<=r):
            mid = (l+r) // 2
            print('mid:',nums[l],nums[mid],nums[r])
            if nums[l] <= nums[r]: return nums[l]

            ans = min(ans, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

            