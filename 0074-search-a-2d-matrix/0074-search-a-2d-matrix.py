class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low, high = 0, len(matrix) - 1
        row = 0
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        print('row:',matrix[row])
        l,r = 0, len(matrix[0]) - 1
        while (l <= r):
            mid = (l + r) // 2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
