class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_idx = 0
        curr_furthest_idx = 0
        next_furthest_idx = 0
        step = 0
        while curr_idx < len(nums):
            if curr_furthest_idx >= len(nums) - 1:
                break

            next_furthest_idx = max(next_furthest_idx, nums[curr_idx] + curr_idx)
            if curr_idx == curr_furthest_idx:
                step += 1
                curr_furthest_idx = next_furthest_idx

            curr_idx += 1

        return step
