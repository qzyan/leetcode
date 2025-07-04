class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [{} for _ in range(k + 1)]
        prev_res = [0] * (k + 1)
        res = [0] * (k + 1)

        for num in nums:
            for i in range(k + 1):
                dp[i][num] = dp[i].get(num, 0) + 1
                dp[i][num] = max(dp[i][num], (prev_res[i - 1] + 1 if i else 1))
                res[i] = max(prev_res[i], dp[i][num])
            
            prev_res = res
            res = [0] * (k + 1)
        
        return prev_res[k]


