class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_max = nums[0]
        no_rob = 0

        for i in range(1, len(nums)):
            prev_max = curr_max
            curr_max = max(no_rob + nums[i], curr_max)
            no_rob = prev_max

        return curr_max