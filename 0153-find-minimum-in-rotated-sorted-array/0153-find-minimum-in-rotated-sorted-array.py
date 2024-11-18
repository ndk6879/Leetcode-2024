class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1  
        ans = nums[0]
        while (l<=r):
            # if l~r portion is sorted 
            if nums[l] <= nums[r]: 
                return min(nums[l], ans) 

            # if not sorted
            mid = (l+r) // 2
            ans = min(ans, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

            