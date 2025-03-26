class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        l = 0
        ans = []
        #[-4, -1, -1, 0, 1, 2]
        for l in range(len(nums)-2):
            if l > 0 and nums[l] == nums[l-1]: continue
            
            i = l + 1
            r = l + 2
            while(r < len(nums)):
                total = nums[l] + nums[i] + nums[r]

                if total == 0:
                    ans.append([nums[l] , nums[i] , nums[r]])

                    while(r+1 < len(nums) and nums[r] == nums[r+1] ):
                        r+=1

                r += 1

        return ans