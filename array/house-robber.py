class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        rob = nums[0]
        no_rob = 0

        for i in range(1, len(nums)):
            prev_rob = rob
            rob = no_rob + nums[i]
            no_rob = prev_rob

        return max(rob, no_rob)