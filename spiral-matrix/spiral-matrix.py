class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_size = len(matrix)
        col_size = len(matrix[0])
            
        start_row = 0
        start_col = 0
        end_row = row_size - 1
        end_col = col_size - 1
        result = []
        
        while start_row <= end_row and start_col <= end_col: 
            for col_idx in range(start_col, end_col + 1):
                result.append(matrix[start_row][col_idx])

            for row_idx in range(start_row + 1, end_row + 1):
                result.append(matrix[row_idx][end_col])

            for col_idx in range(end_col - 1, start_col - 1, -1):
                if start_row == end_row:
                    break
                    
                result.append(matrix[end_row][col_idx])

            for row_idx in range(end_row - 1, start_row, -1):
                if start_col == end_col:
                    break
                result.append(matrix[row_idx][start_col])

            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1
        
        return result