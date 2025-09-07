class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -float("inf")
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum