class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        arr = [False] * len(nums)
        ans = []
        cur = []

        def dfs(arr):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return

            for i in range(len(arr)):
                if not arr[i]:
                    arr[i] = True
                    cur.append(nums[i])
                    dfs(arr)
                    cur.pop()
                    dfs(arr)
                    arr[i] = False
            


        dfs(arr)
        return ans