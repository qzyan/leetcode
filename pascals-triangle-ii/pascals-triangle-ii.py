class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = [1]
        for i in range(1, rowIndex + 1):
            curr = [0] * (i + 1)
            curr[0] = curr[-1] = 1
            for j in range(1, i):
                curr[j] = prev[j - 1]+ prev[j]
            
            prev = curr
            
        return prev