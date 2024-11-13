class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1. Find min in usual binary search and see if mid is minimum

        2. if not case1, determine to search left portion or right portion
        2-1. we search right if nums[l] <= nums[mid] b/c this means left porition is sorted in increasing order (i.e. l = mid + 1)
        2-2. Otherwise, just search left portion (i.e. r = mid - 1)
        '''

        if len(nums) == 1: return nums[-1]
        l = 0
        r = len(nums) - 1 
        ans = nums[0]
        while(l<=r):
            mid = (l + r) // 2
            if nums[l] <= nums[mid] <= nums[r]:
                ans = min(ans, nums[l])
                break

            ans = min(ans, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return ans