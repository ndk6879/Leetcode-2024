class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = {}
        for ind,num in enumerate(nums):
            if target - num not in adict:
                adict[num] = ind

            else:
                return [adict[target - num],ind]
