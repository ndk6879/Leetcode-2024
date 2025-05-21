from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = board[r][c]

                if board[r][c] == '.': continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]: 
                    return False
                
                rows[r].add(cur)
                cols[c].add(cur)
                square[(r//3,c//3)].add(cur)
        return True

