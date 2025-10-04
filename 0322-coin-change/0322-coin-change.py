class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [amount+1] * (amount+1)
        arr[0]=0
        for i in range(len(arr)):
            for c in coins:
                if (i - c) >= 0:
                    arr[i] = min(arr[i-c] + 1, arr[i])
        print('arr:',arr)

        return arr[-1] if arr[-1] != amount else -1