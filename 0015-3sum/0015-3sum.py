class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        '''
        1. sort array
        2. use two pointers l,r to check if the sum of window is 0
        '''

        nums.sort()
        ans = []
        for l in range(len(nums)-2):
            i = l + 1
            r = len(nums) - 1
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            
            while (i < r):
                total = nums[l] + nums[i] + nums[r]

                if total == 0:
                    ans.append([nums[l] , nums[i] , nums[r]])
                    i += 1

                    while (i < r and nums[r] == nums[r-1]):
                        i += 1
                
                elif total < 0:
                    i += 1

                else:
                    r -= 1
        return ans