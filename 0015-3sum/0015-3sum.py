class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        #nums = [-4, -1, -1, 0, 1, 2]
        
        ans = []
        for l in range(len(nums)):

            if l > 0 and nums[l] == nums[l - 1]:
                continue

            i = l + 1
            r = len(nums) - 1
            
            
            while (i < r):
                total = nums[l] + nums[i] + nums[r]
                if total == 0:
                    ans.append([nums[l],nums[i],nums[r]])
                    i += 1
                    while i < r and nums[i] == nums[i-1]:
                        i += 1

                elif total < 0:
                    i += 1

                elif total > 0: #else
                    r -= 1

        return ans  