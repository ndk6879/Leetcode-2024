class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        subSet = []

        def dfs(i):
            if i >= len(nums):
                ans.append(subSet[:])
                return
            
            subSet.append(nums[i])
            dfs(i+1)

            subSet.pop()
            dfs(i+1)


        dfs(0)
        return ans