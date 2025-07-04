class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        dp = [[1] * len(nums) for _ in range(k + 1)]
        for i in range(k + 1):
            for j in range(len(nums)):
                for p in range(j):
                    if nums[j] == nums[p]:
                        dp[i][j] = max(dp[i][j], dp[i][p] + 1)
                    else:
                        if i - 1 >= 0:
                            dp[i][j] = max(dp[i][j], dp[i - 1][p] + 1)
                        else:
                            dp[i][j] = max(dp[i][j], 1)

        return max(dp[k]) 