class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return False

            if grid[i][j] == '1':
                grid[i][j] = '#'
                dfs(i-1,j) 
                dfs(i+1,j) 
                dfs(i,j-1) 
                dfs(i,j+1)
                return True
            return False



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j):
                    ans += 1
        return ans 
        