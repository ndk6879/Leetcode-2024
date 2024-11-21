class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        print('nums:',nums)
        ans = []
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while(l<r):
                total = nums[l] + nums[i] + nums[r]
                # print(nums[i],nums[l],nums[r])
                if total == 0:
                    print('yes')
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while(l < r and nums[l-1] == nums[l]): 
                        l+=1
                
                elif total > 0:
                    r -= 1

                else:
                    l += 1

        return ans