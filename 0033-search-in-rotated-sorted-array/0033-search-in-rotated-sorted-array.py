class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        ans = nums[0]

        while(l<=r):
            mid = (l + r) // 2
         
            print(nums[mid])
            if nums[mid] == target:
                return min(ans,mid)
            
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            
            else:
                l = mid + 1
        return -1