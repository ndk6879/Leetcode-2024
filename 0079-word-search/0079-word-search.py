class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            

            if not (0 <= i < len(board)) or \
               not (0 <= j < len(board[0])) or \
               board[i][j] != word[k]:  # Invalid path
                # print('wrong', i, j, k)
                return False  # Return False here

            # print('true', i, j, k)

            tmp = board[i][j]
            board[i][j] = '#'
            # Explore all 4 directions
            if k == len(word) - 1: 
                # print('oh yeah')
                return True  # Found the word

            if dfs(i + 1, j, k + 1) or \
               dfs(i - 1, j, k + 1) or \
               dfs(i, j + 1, k + 1) or \
               dfs(i, j - 1, k + 1):
                return True  # Return True if any direction works
            board[i][j] = tmp
            return False  # Return False if none of the directions work

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): 
                    return True
        
        return False
