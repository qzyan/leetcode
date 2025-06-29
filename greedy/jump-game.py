class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_idx = 0
        furthest_idx = 0
        while curr_idx <= furthest_idx:
            if furthest_idx >= len(nums) - 1:
                return True
            
            furthest_idx = max(furthest_idx, nums[curr_idx] + curr_idx)
            curr_idx += 1

        return False