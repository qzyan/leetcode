class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        comb = []
        combs = []
        self.back_tracking(nums, 0, comb, combs)
        return combs
    
    def back_tracking(self, nums, start_idx, comb, combs):
        # a vaild subseq
        if len(comb) >= 2:
            combs.append(comb[:])
        visited = set()
        # iterate over the nums starting from the start_idx
        for idx in range(start_idx, len(nums)):
            # nums[idx] will make the comb desc
            if comb and nums[idx] < comb[-1]:
                continue
            
            # duplicate comb
            if nums[idx] in visited:
                continue
            
            visited.add(nums[idx])
            
            comb.append(nums[idx])
            self.back_tracking(nums, idx + 1, comb, combs)
            comb.pop()
        
            
            