class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                ind, temp = stack.pop()
                ans[ind] = i - ind
            
            stack.append([i,t])

        return ans