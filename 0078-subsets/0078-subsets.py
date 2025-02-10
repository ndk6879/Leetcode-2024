from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            for j in (list(combinations(nums,i+1))):
                ans.append(j)

        return ans