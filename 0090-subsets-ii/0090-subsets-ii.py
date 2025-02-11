class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur = []
        ans = []



        def dfs(i):
            
            if i >= len(nums):
                if cur.copy() not in ans:
                    ans.append(cur.copy())
                return



            cur.append(nums[i])
            dfs(i+1)

            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        dfs(0)
        return ans