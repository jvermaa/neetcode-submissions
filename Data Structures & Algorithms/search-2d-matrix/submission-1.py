class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0

        ROWS = len(matrix)
        COLS = len(matrix[0])

        right = ROWS * COLS - 1 

        while left <= right:
            
            if matrix[left//COLS][left % COLS] == target:
                return True
            
            if matrix[right//COLS][left % COLS] == target:
                return True
            
            mid = (left + right) // 2
            r = mid // COLS
            c = mid % COLS
            
            if matrix[r][c] < target:
                left = mid + 1
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                return True
        
        return False