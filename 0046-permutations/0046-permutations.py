class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        subSet = []

        def dfs():

            if len(subSet) == len(nums):
                ans.append(subSet.copy())
                return
            
            for num in nums:
                if num in subSet:
                    continue

                subSet.append(num)                
                dfs()
                subSet.pop()
        
        dfs()
        return ans