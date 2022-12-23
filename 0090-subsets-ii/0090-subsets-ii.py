class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        if len(nums) == 1:
            return [[], nums[:]]
        
        nums = sorted(nums)
        combs = [[], nums[:1]]
        prev_combs = [nums[:1]]
        
        for idx in range(1, len(nums)):
            prev_num = nums[idx - 1]
            num = nums[idx]
            
            if prev_num != num:
                new_combs = [comb + [num] for comb in combs]
            else:
                new_combs = [comb + [num] for comb in prev_combs]
            
            combs.extend(new_combs)
            prev_combs = new_combs
        
        return combs
        