class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # 1. 각 자리 = cost[i] + min(i-1,i-2) 
        # 2. 각 자리에 올수있는 애들은 i-2,i-1
        # 3. top = 마지막 index+1의 위치구나

        arr = [0 for _ in range(len(cost))]
        arr[0] = cost[0]
        arr[1] = cost[1]

        for i in range(2,len(arr)):
            arr[i] = cost[i] + min(arr[i-1],arr[i-2])
        
        print(arr)
        return min(arr[-2],arr[-1])