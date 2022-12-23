class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        comb = []
        combs = [[]]
        self.backtrack(nums, comb, combs, 0)
        return combs
        
    def backtrack(self, nums, comb, combs, start_idx):
        for idx in range(start_idx, len(nums)):
            num = nums[idx]
            comb.append(num)
            combs.append(comb[:])
            self.backtrack(nums, comb, combs, idx + 1)
            comb.pop()
        return
        
        