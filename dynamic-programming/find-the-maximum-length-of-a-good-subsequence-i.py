class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[1] * len(nums) for _ in range(k + 1)]
        res = 1
        for row in range(k + 1):
            dp[row][0] = 1
            for col in range(1, len(nums)):
                for j in range(col):
                    if nums[col] == nums[j]:
                        dp[row][col] = max(dp[row][j] + 1, dp[row][col])
                    else:
                        dp[row][col] = max(dp[row - 1][j] + 1 if row else 1, dp[row][col])

                    res = max(res, dp[row][col])

        return res

            