class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()

        def dfs(index,path):

            if index == len(nums): 
                ans.append(path[:])
                return

            path.append(nums[index])
            dfs(index+1,path)
            path.pop()

            while index + 1 < len(nums) and nums[index+1] == nums[index]:
                index += 1
            dfs(index+1,path)


        dfs(0,[])
        return ans