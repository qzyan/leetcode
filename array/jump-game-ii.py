class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for idx in range(len(nums)):
            if dp[idx] == float("inf"):
                continue
            
            for step in range(1, nums[idx] + 1):
                if step + idx  == len(nums) - 1:
                    return dp[idx] + 1
                if step + idx < len(nums):
                    dp[step + idx] = min(dp[step + idx], dp[idx] + 1)

        return dp[-1]