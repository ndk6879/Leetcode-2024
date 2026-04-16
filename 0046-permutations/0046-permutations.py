class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans, cur = [], []

        def dfs(i):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            if i >= len(nums):
                return

            for num in nums:
                if num in cur:
                    continue
                
                cur.append(num)
                dfs(i+1)
                cur.pop()
                dfs(i+1)

        dfs(0)
        return ans