class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()

        def dfs(i,j,visit,prevheight):
            if (i < 0 or 
            i >= len(heights) or
            j < 0 or 
            j >= len(heights[0]) or
            ((i,j)) in visit or
            heights[i][j] < prevheight
            ): return

            visit.add((i,j))
            dfs(i-1,j,visit,heights[i][j])
            dfs(i+1,j,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            return True


        for i in range(len(heights)):
            dfs(i,0,pac,heights[i][0])
            dfs(i,len(heights[0])-1,atl,heights[i][-1])

        for i in range(len(heights[0])):
            dfs(0,i,pac,heights[0][i])
            dfs(len(heights)-1,i,atl,heights[-1][i])

        
        ans = []
        for i in pac:
            if i in atl:
                ans.append(i)
        print('ans:',ans)

        return ans

        