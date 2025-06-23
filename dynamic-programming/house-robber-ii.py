class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max1 = self.helper(nums, 0, len(nums) - 2)
        max2 = self.helper(nums, 1, len(nums) - 1)
        return max(max1, max2)

    def helper(self, nums, start, end):
        curr_max = nums[start]
        prev_max = 0
        for i in range(start + 1, end + 1):
            prev_curr_max = curr_max
            curr_max = max(curr_max, nums[i] + prev_max)
            prev_max = prev_curr_max

        return curr_max
