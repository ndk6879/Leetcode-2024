class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        cur = []

        def dfs(i):
            
            if cur not in ans:
                ans.add(cur.copy())
                return

            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)

        dfs(0)
        return ans