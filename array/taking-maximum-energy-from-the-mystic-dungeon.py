class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [-float("inf")] * len(energy)
        res = -float("inf")
        for idx in range(len(dp)):
            dp[idx] = max(energy[idx], dp[idx - k] + energy[idx] if idx - k >= 0 else -float("inf"))
            
            if idx + k >= len(energy):
                res = max(res, dp[idx])
                    
        return res