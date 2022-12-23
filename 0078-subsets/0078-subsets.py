class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        comb = []
        combs = []
        self.backtrack(nums, comb, combs, 0)
        return combs
        
    def backtrack(self, nums, comb, combs, start_idx):
        combs.append(comb[:])

        for idx in range(start_idx, len(nums)):
            num = nums[idx]
            comb.append(num)
            self.backtrack(nums, comb, combs, idx + 1)
            comb.pop()
            
        return
        
        