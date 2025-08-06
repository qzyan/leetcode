# fn(1, n) = min
#   1 + max(fn(1, 0), fn(2, n)), 
#   2 + max(fn(1, 1), fn(3, n)),
#.  3 + max(fn(1, 2), fn(4, n)),
#.  .....
#.  n + max(fn(1, n - 1), fn(n + 1, n))

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return self.dfs(1, n, {})

    def dfs(self, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]

        if start >= end:
            return 0
        
        res = float("inf")
        for i in range(start, end):
            curr_res = i + max(self.dfs(start, i - 1, memo), self.dfs(i + 1, end, memo))
            res = min(res, curr_res)

        memo[(start, end)] = res
        return res