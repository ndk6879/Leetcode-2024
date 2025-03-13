class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for ind, val in enumerate(temperatures):

            while stack and val > stack[-1][-1]:
                cur = stack.pop()
                i, v = cur[0], cur[1]
                ans[i] = ind - i

            stack.append([ind,val])
        
        return ans