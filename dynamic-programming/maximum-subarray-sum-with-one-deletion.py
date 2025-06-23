class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [[0] * len(arr) for i in range(2)]
        dp[0][0] = arr[0]
        dp[1][0] = 0
        max_sum = arr[0]

        for i in range(1, len(arr)):
            dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
            dp[1][i] = max(dp[1][i - 1] + arr[i], dp[0][i - 1])
            max_sum = max(max_sum, dp[0][i], dp[1][i])

        return max_sum