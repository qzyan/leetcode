class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_idx = 0
        furthest_idx = 0
        step = 0
        while furthest_idx < len(nums) - 1:
            new_furthest_idx = furthest_idx
            
            while curr_idx <= furthest_idx:
                new_furthest_idx = max(new_furthest_idx, curr_idx + nums[curr_idx])
                curr_idx += 1
            
            step += 1
            furthest_idx = new_furthest_idx
        
        return step