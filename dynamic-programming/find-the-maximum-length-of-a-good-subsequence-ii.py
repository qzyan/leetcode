class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [{} for _ in range(k + 1)]
        res = [0] * (k + 1)

        for num in nums:
            for i in range(k + 1):
                if num not in dp[i]:
                    dp[i][num] = res[i - 1] + 1 if i else 1
                else:
                    dp[i][num] = max(dp[i][num], res[i - 1] if i else 0) + 1

            for j in range(k + 1):
                res[j] = max(res[j], dp[j][num])
            
            

        return res[k]