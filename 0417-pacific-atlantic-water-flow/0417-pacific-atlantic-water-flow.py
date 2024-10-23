class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        columns = len(heights[0])

        def dfs(r,c,visit,prevheight):
            if (r < 0 or 
            r == rows or
            c < 0 or 
            c == columns or
            (r,c) in visit or
            heights[r][c] < prevheight):
                return

            visit.add((r,c))

            '''
            일단 끝쪽에 있는 애들. i.e. 최소한 either pacific ocean or atl ocean에
            인접한 애들로부터 dfs를 시작. 그러고 얘들이 동서남북으로 traverse 한다는건 traverse
            하는 방향인 애는 현재값보다는 크다는 거고 걔는 현재 visit값에는 포함 될 수 있음.
            만약 atl과 pac에 둘다 포함되는 height[r][c]는 모든 ocean에 갈 수 있음. 
            '''
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
        
        for c in range(columns):
            dfs(0,c,pac,heights[0][c]) #첫번째 row를 pacific에 추가
            dfs(rows-1,c,atl,heights[rows-1][c]) #마지막 row를 atl에 추가

        for r in range(rows):
            dfs(r,0,pac,heights[r][0]) #첫번째 col를 pacific에 추가
            dfs(r,columns-1,atl,heights[r][columns-1]) #마지막 col를 atl에 추가


        ans = []
        for i in range(rows):
            for j in range(columns):
                if (i,j) in atl and (i,j) in pac:
                    ans.append([i,j])
        
        return ans