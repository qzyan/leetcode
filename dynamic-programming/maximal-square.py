class GridType:
    ISLAND = "1"
    WATER = "0"

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_len = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == GridType.WATER:
                    continue
                
                prev1 = dp[row - 1][col] if row - 1 >= 0 else 0
                prev2 = dp[row][col - 1] if col - 1 >= 0 else 0
                prev3 = dp[row - 1][col - 1] if row - 1 >= 0 and col - 1 >= 0 else 0
                dp[row][col] = min(prev1, prev2, prev3) + 1
                max_len = max(dp[row][col], max_len)

        return max_len ** 2
