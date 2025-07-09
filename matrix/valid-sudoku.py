class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]:
            return False

        digits_in_rows = [set() for _ in range(9)]
        digits_in_cols = [set() for _ in range(9)]
        digits_in_submatrixs = [set() for _ in range(9)]

        for r_idx in range(9):
            for c_idx in range(9):
                if board[r_idx][c_idx] == ".":
                    continue

                digit = int(board[r_idx][c_idx])
                if digit < 1 or digit > 9:
                    return False
                if digit in digits_in_rows[r_idx]:
                    return False
                if digit in digits_in_cols[c_idx]:
                    return False
                if digit in digits_in_submatrixs[r_idx // 3 * 3 + c_idx // 3]:
                    return False
                
                digits_in_rows[r_idx].add(digit)
                digits_in_cols[c_idx].add(digit)
                digits_in_submatrixs[r_idx // 3 * 3 + c_idx // 3].add(digit)

        return True
