class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix) - 1
        while(bottom <= top):
            row = (bottom + top) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            
            elif matrix[row][0] > target:
                top = row - 1
                print('top:',top)

            else:
                bottom = row + 1
                print('bottom:',bottom)
        
        print('row:',row)

        l, r = 0, len(matrix[0]) - 1
        while (l <= r):
            mid = (l+r)//2
            print('matrix[row][mid]:',l,r,matrix[row][mid])
            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
                

        return matrix[row][mid] == target