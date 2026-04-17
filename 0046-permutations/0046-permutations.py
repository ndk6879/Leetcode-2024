class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        ans = []
        subSet = []

        def dfs(i):
            if len(subSet) == len(nums):
                ans.append(subSet[:])
                return

            if i >= len(nums):
                return

            for num in nums:
                if num in subSet:
                    continue

                subSet.append(num)
                dfs(i+1)
                subSet.pop()
                dfs(i+1)


        dfs(0)
        return ans