class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [amount+1] * (amount+1)
        arr[0] = 0
        
        for i in range(len(arr)):
            for coin in coins:
                if (i-coin) >= 0:
                    arr[i] = min(arr[i],arr[i-coin] + 1)
        
        if arr[-1] == amount+1: return -1
        return arr[-1]