class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0

        def dfs(i,j):
            if (i < 0 or len(grid) <= i or
            j < 0 or len(grid[0]) <= j or
            grid[i][j] == '0'):
                return False

            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)            

            return True
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j):
                    ans += 1

        return ans 