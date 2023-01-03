class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs or not strs[0]:
            return 0
        
        count = 0
        col_size = len(strs[0])
        for col_idx in range(col_size):
            if self.is_sorted(strs, col_idx):
                continue
            count += 1
        
        return count
    
    def is_sorted(self, strs, col_idx):
        for row_idx in range (len(strs) - 1):
            if strs[row_idx][col_idx] > strs[row_idx + 1][col_idx]:
                return False
        
        return True
            
        