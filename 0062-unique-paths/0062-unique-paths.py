class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(0)
            arr.append(tmp)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
            
        
        return arr[-1][-1]