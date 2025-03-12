from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]

                if value == '.': continue

                if value in rows[r] or value in cols[c] or value in squares[(r,c)]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[(r,c)].add(value)

        return True