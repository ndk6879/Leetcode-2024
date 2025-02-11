class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i,j,cnt):
            if (i < 0 or 
            i >= len(board) or
            j < 0 or 
            j >= len(board[0]) or
            cnt >= len(word) or
            board[i][j] != word[cnt]):
                return False

            if cnt == len(word)-1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'
            
            if dfs(i+1,j,cnt+1) or dfs(i-1,j,cnt+1) or dfs(i,j-1,cnt+1) or dfs(i,j+1,cnt+1):
                return True
            board[i][j] = tmp


        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True

        return False
        