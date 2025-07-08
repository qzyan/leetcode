class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [e for e in energy]

        for idx in range(len(dp)):
            dp[idx] = max(dp[idx], dp[idx - k] + energy[idx] if idx >= k else energy[idx])

        return max(dp[len(dp) - k:])

