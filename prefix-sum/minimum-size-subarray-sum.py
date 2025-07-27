class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right = 0, 0
        sum_val = 0
        min_len = float("inf")
        while right < len(nums):
            sum_val += nums[right]
            right += 1

            while left < right and sum_val >= target:
                min_len = min(min_len, right - left)
                sum_val -= nums[left]
                left += 1
            
        return min_len if min_len != float("inf") else 0