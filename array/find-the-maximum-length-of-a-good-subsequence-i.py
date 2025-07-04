class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        dp = [{} for _ in range(k + 1)]
        res = [0] * (k + 1)

        for num in nums:
            for i in range(k, -1, -1):
                dp[i][num] = max(dp[i][num] + 1 if num in dp[i] else 1, res[i - 1] + 1 if i else 0)
                res[i] = max(res[i], dp[i][num])

        return res[k]