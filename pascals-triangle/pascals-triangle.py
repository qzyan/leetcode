class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[0] * n for n in range(1, numRows + 1)]
        for i in range(numRows):
            result[i][0] = 1
            result[i][-1] = 1
            if i > 1:
                for j in range(1, i):
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
                
        return result
        