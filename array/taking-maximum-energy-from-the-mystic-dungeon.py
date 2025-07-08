class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        result = -float("inf")
        for idx in range(len(energy) - 1, -1 ,- 1):
            dp[idx] = energy[idx] + (dp[idx + k] if idx + k < len(energy) else 0)
            result = max(result, dp[idx])

        return result

