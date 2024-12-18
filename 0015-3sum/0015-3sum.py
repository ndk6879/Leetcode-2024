class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print('nums:',nums)

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            #[-4,-1,-1,0,1,2]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while(l<r):
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[i] , nums[l] , nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif total < 0:
                    l += 1
                
                else:
                    r -= 1
        return ans