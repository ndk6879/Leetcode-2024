class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        ans = []

        # [-4,-1,-1,0,1,2]
        for l in range(len(nums)-2):
            i = l + 1
            r = len(nums) - 1
            
            if l > 0 and nums[l] == nums[r]:
                continue

            while(i < r):
                total = nums[l] + nums[i] + nums[r]
                if total == 0:
                    ans.append([nums[l] , nums[i] , nums[r]])
                    while i < r and nums[l] == nums[i]:
                        i += 1
                    i += 1
                 
                elif total < 0:
                    i += 1
                
                elif total > 0:
                    r -= 1

                


        return ans