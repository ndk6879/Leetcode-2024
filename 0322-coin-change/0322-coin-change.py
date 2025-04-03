class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        arr = [amount + 1] * (amount+1)
        arr[0] = 0

        for i in range(1,len(arr)):
            for coin in coins:
                if i-coin >=0:
                    arr[i] = min(arr[i-coin] + 1, arr[i])

        return arr[-1] if arr[-1] != amount+1 else -1