class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            dp[0][i] = i
        
        for i in range(len(word2) + 1):
            dp[i][0] = i

        for row in range(1, len(word2) + 1):
            for col in range(1, len(word1) + 1):
                if word1[col - 1] == word2[row - 1]:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col - 1])
                else:
                    min_prev = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                    dp[row][col] = min(dp[row][col], min_prev + 1)

        return dp[-1][-1]