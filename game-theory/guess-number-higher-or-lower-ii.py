''' 
    n-3
   /    \ 
        n-1
       /    \
      n-2    n
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for row in range(n, 0, -1):
            for col in range(row + 1, n + 1):
                res = float("inf")
                for k in range(row, col):
                    opt1 = dp[row][k - 1]
                    opt2 = dp[k + 1][col]
                    cost = max(opt1, opt2) + k
                    res = min(cost, res)

                dp[row][col] = res

        return dp[1][n]