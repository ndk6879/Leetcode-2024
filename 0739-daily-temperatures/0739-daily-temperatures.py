class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0 for _ in range(len(temperatures))]

        for ind, val in enumerate(temperatures):

            while stack and stack[-1][-1] < val:
                i = stack[-1][0]
                temp = ind - stack[-1][0]
                ans[i] = temp
                stack.pop()
            stack.append([ind, val])

        return ans