class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # 최소값은 오른쪽 절반에 있음
                left = mid + 1
            else:
                # 최소값은 왼쪽 절반에 있음 (mid 포함 가능)
                right = mid
        
        return nums[left]