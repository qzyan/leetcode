class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        is_row0_0, is_col0_0 = self.mark_0_rows_and_cols(matrix)

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                
        if is_row0_0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        if is_col0_0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

    def mark_0_rows_and_cols(self, matrix):
        is_row0_0, is_col0_0 = False, False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                is_col0_0 = True
        
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                is_row0_0 = True
        
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        return is_row0_0, is_col0_0

        
        