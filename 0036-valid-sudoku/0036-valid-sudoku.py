from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):

                cur = board[r][c]
                if cur == '.': continue
                if cur in row[r]: return False
                if cur in col[c]: return False
                if cur in square[((r//3),(c//3))]: return False

                row[r].add(cur)
                col[c].add(cur)
                square[((r//3),(c//3))].add(cur)
                
        return True