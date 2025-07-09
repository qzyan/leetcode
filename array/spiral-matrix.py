class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        lt_row, lt_col = 0, 0
        rb_row, rb_col = len(matrix) - 1, len(matrix[0]) - 1
        results = []
        while lt_row < rb_row and lt_col < rb_col:
            for col in range(lt_col, rb_col + 1):
                num = matrix[lt_row][col]
                results.append(num)

            for row in range(lt_row + 1, rb_row):
                num = matrix[row][rb_col]
                results.append(num)

            for col in range(rb_col, lt_col - 1, -1):
                num = matrix[rb_row][col]
                results.append(num)

            for row in range(rb_row - 1, lt_row, -1):
                num = matrix[row][lt_col]
                results.append(num)

            lt_row += 1
            lt_col += 1
            rb_row -= 1
            rb_col -= 1

        if lt_row == rb_row:
            for col in range(lt_col, rb_col + 1):
                num = matrix[lt_row][col]
                results.append(num)
        elif lt_col == rb_col:
            for row in range(lt_row, rb_row + 1):
                num = matrix[row][rb_col]
                results.append(num)

        return results
