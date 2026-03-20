class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        '''
        1. use 2 for loops to iterate over on ea ch character
        2. do dfs on each character 
        3. return False if none of character matches or return true at 
        '''

        visit = set()
        def dfs(cnt,i,j):

            if cnt == len(word):
                return True
            
            if (i < 0 or i >= len(board) or
            j < 0 or j >= len(board[0]) or 
            board[i][j] != word[cnt] or 
            (i,j) in visit
            ):
                return False

            visit.add((i,j))

            res = (dfs(cnt+1,i-1,j) or dfs(cnt+1,i+1,j) or dfs(cnt+1,i,j-1) or dfs(cnt+1,i,j+1))
            visit.remove((i,j))

            return res

            



        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0,i,j):
                    return True
        
        return False