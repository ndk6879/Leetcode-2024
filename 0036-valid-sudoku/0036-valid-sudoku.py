from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)


        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = board[r][c]
                
                if cur == '.': continue
                if cur in rows[r]: 
                    print('rows' , cur ,  rows[r])
                    return False
                if  cur in cols[c]: 
                    print('cols')
                    return False
                if  cur in squares[( r//3 , c//3  )] : 
                    print('squares')
                    return False

                


                rows[r].append(cur)
                cols[c].append(cur)
                squares[ (r//3, c//3)  ].append(cur)
        return True