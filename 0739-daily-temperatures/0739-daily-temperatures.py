class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        queue = []

        for ind,t in enumerate(temperatures):
            while queue and queue[-1][-1] < t:
                curInd, curT = queue.pop()
                ans[curInd] = ind - curInd

            queue.append([ind, t])

        return ans