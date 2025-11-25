class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #1. if total gas < total cost: return -1

        #2. if gas[i] - cost[i] < 0: increment i by 1 bc i can't be answer

        if sum(gas) - sum(cost) < 0: return -1

        ans = 0
        for i in range(len(gas)):
            if gas[i] - cost[i] < 0:
                ans = i + 1
        
        if ans == len(gas): return 0
        else: return ans