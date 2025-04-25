class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def dfs(index, path):
            if index == len(nums):
                ans.append(path[:])
                return 

            path.append(nums[index])
            dfs(index + 1,path)
            path.pop()
            dfs(index+1,path)
        
        dfs(0, [])
        return ans