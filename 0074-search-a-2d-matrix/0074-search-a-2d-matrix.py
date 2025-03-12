class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                row = i
                
        
        l,r = 0, len(matrix[row])-1

        while(l<=r):
            mid = (l+r) // 2
            if matrix[row][mid] == target: return True

            elif matrix[row][mid] < target: 
                l = mid + 1

            else:
                r = mid - 1

        return False