class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curr_sum = 0
        max_sum = -float('inf')
        for num in nums:
            # if the prev_sum is neg, reset to 0
            # dp[i] = max(dp[i - 1], 0) + nums[i]
            curr_sum = max(curr_sum, 0) + num
            max_sum = max(max_sum, curr_sum)
                
        return max_sum
            
                