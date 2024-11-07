class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        '''
        #1. create set for pacific ocean and atlantic ocean
        #2. add each proper coordinate in set
        #3. if a coordinate is in both set, add it as answer
        '''
        pacificSet = set()
        atlanticSet = set()

        def dfs(i,j,visit,prevheight):
            if (i < 0 or 
            i >= len(heights) or
            j < 0 or 
            j >= len(heights[0]) or
            (i,j) in visit or
            heights[i][j] < prevheight):
                return

            visit.add((i,j))
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i+1,j,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
        
        for i in range(len(heights)):
            dfs(i,0,pacificSet,heights[i][0]) #첫번째 column
            dfs(i,len(heights[0])-1,atlanticSet,heights[i][len(heights[0])-1]) #마지막 column

        for i in range(len(heights[0])):
            dfs(0,i,pacificSet,heights[0][i])
            dfs(len(heights)-1,i,atlanticSet,heights[len(heights)-1][i])

        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in atlanticSet and (i,j) in pacificSet:
                    ans.append([i,j])
        return ans