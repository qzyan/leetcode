class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_subarray_total = -float("inf")
        min_subarray_total = float("inf")
        curr_subarray_max = -float("inf")
        curr_subarray_min = float("inf")

        for num in nums:
            curr_subarray_max = max(curr_subarray_max + num, num)
            curr_subarray_min = min(curr_subarray_min + num, num)

            max_subarray_total = max(max_subarray_total, curr_subarray_max)
            min_subarray_total = min(min_subarray_total, curr_subarray_min)

        total = sum(nums)

        max2 = total - min_subarray_total

        if max2 == 0:
            return max_subarray_total

        return max(max_subarray_total, max2)