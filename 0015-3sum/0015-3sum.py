class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort() # [-4,-1,-1,0,1,2]
        print('nums:',nums)

        for l in range(len(nums)-2):
            i = l + 1

            if l > 0 and nums[l] == nums[l-1]:
                continue
            # print('new L')
            r = len(nums) - 1
            while (i < r):
                # print([nums[l],nums[i],nums[r]])
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[l],nums[i],nums[r]])
                    i += 1
                    while (nums[i] == nums[i-1] and i < r):
                        i += 1
                        

                elif total > 0:
                    r -= 1

                elif total < 0:
                    i += 1

                

        return ans
        