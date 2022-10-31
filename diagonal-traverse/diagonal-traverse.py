class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        is_up = True
        row_size = len(mat)
        col_size = len(mat[0])
        row_idx = 0
        col_idx = 0
        
        while 0 <= row_idx < row_size and 0 <= col_idx <= col_size:
            result.append(mat[row_idx][col_idx])
            
            if row_idx == row_size - 1 and col_idx == col_size - 1:
                break
            
            if is_up and col_idx == col_size - 1:
                is_up = not is_up
                row_idx += 1
                continue
            
            if is_up and row_idx == 0:
                is_up = not is_up
                col_idx += 1
                continue
            
            if not is_up and row_idx == row_size - 1:
                is_up = not is_up
                col_idx += 1
                continue
            
            if not is_up and col_idx == 0:
                is_up = not is_up
                row_idx += 1
                continue
                
                
            if is_up:
                row_idx -= 1
                col_idx += 1
            
            else: 
                row_idx += 1
                col_idx -= 1

            
        
        
        return result