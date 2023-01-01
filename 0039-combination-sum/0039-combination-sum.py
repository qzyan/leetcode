class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        combs = []
        self.backtrack(candidates, target, comb, combs, 0)
        return combs
        
    def backtrack(self, candidates, target, comb, combs, start_idx):
        if target < 0:
            return
        if target == 0:
            combs.append(comb[:])
            return
        
        for idx in range(start_idx, len(candidates)):
            comb.append(candidates[idx])
            self.backtrack(candidates, target - candidates[idx], comb, combs, idx)
            comb.pop()
        
        return
    