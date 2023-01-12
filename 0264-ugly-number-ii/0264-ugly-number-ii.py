class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        
        while len(dp) < n:
            next_ugly_num = min(
                dp[p2] * 2,
                dp[p3] * 3,
                dp[p5] * 5
            )
            
            dp.append(next_ugly_num)
            
            if next_ugly_num == dp[p2] * 2:
                p2 += 1
            if next_ugly_num == dp[p3] * 3:
                p3 += 1
            if next_ugly_num == dp[p5] * 5:
                p5 += 1
        
        return dp[-1]