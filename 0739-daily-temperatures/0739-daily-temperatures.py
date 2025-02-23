class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):


            while stack and temp > stack[-1][-1]:
                print(temp , stack[-1][-1])
                i, tmp = stack.pop()
                ans[i] = ind - i


            stack.append((ind, temp))

        return ans