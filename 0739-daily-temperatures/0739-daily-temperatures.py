class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Use stack = []
        for loop:
            append(temperature)
            if stack and cur_temp > temperature_in_stack:
                a
        
        '''
        ans = [0 for _ in range(len(temperatures))]
        stack = []

        for ind,val in enumerate(temperatures):
            while stack and val > stack[-1][-1]:
                cur = stack.pop()
                i,t = cur[0], cur[1]
                ans[i] = ind - i

            stack.append([ind,val])
        return ans