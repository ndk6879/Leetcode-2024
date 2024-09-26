class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # [-4,-1,-1,0,1,2]
        print('nums:',nums)
        ans = []
        
        for l in range(len(nums)-2):
            i = l + 1
            r = len(nums) - 1
            if l > 0 and nums[l] == nums[l-1]:
                continue
            
            while(i < r):
                total = nums[l] + nums[i] + nums[r]
                if total == 0:
                    print('l:',l)
                    print('ans:',[nums[l],nums[i],nums[r]])
                    ans.append([nums[l],nums[i],nums[r]])
                    i += 1
                    while i < r and nums[i] == nums[i-1]:
                        i += 1
                    
                elif total > 0:
                    r -= 1

                elif total < 0:
                    i += 1
            print('break while loop')

        return ans
        