class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        num_idx_mapping = {}
        for idx, num in enumerate(nums):
            if num not in num_idx_mapping:
                num_idx_mapping[num] = idx
                continue
            
            if idx - num_idx_mapping[num] <= k:
                return True
            else:
                num_idx_mapping[num] = idx

        return False