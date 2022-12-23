class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        combs = []
        comb = []
        self.backtrack(sorted_nums, 0, combs, comb)
        return combs
    
    def backtrack(self, nums, start_idx, combs, comb):
        combs.append(comb[:])
        
        for idx in range(start_idx, len(nums)):
            if idx > start_idx and nums[idx] == nums[idx - 1]:
                continue
            
            comb.append(nums[idx])
            self.backtrack(nums, idx + 1, combs, comb)
            comb.pop()
            
        return
            
    