class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for idx in range(len(nums)):
            for j in range(idx):
                if nums[j] < nums[idx]:
                    dp[idx] = max(dp[idx], dp[j] + 1)
            
            res = max(res, dp[idx])

        return res
