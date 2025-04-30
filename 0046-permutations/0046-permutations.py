class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(index,path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(index+1,path)
                    path.pop()
                    dfs(index+1,path)
                    used[i] = False

            
        dfs(0,[])
        return res
        