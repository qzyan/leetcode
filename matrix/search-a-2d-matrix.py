class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            num = matrix[row][col]
            if num == target:
                return True
            
            if num > target:
                right = mid
            else:
                left = mid

        if matrix[left // len(matrix[0])][left % len(matrix[0])] == target:
            return True

        if matrix[right // len(matrix[0])][right % len(matrix[0])] == target:
            return True
        
        return False