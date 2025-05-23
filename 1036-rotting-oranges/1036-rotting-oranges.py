from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fresh = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))

                elif grid[i][j] == 1: fresh += 1

        directions = [(1,0), (0,1), (-1,0) , (0,-1) ]
        while q and fresh > 0:
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(4):
                    dx = directions[i][0] + cur[0]
                    dy = directions[i][1] + cur[1]

                    if (dx < 0 or dy < 0 or dx >= len(grid) or dy >= len(grid[0]) or 
                    grid[dx][dy] == 2 or grid[dx][dy] == 0
                    ):
                        continue

                    if grid[dx][dy] == 1:
                        fresh -= 1
                        grid[dx][dy] = 2
                        q.append((dx,dy))
            time += 1

        return time if fresh == 0 else -1