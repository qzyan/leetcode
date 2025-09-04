class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        comb = []
        combs = []
        self.dfs(comb, combs, target, 0, candidates)
        return combs

    def dfs(self, comb, combs, curr_target, start_idx, candidates):
        if curr_target == 0:
            combs.append(comb[:])
            return
        
        if curr_target < 0:
            return

        for idx in range(start_idx, len(candidates)):
            if idx > 0 and candidates[idx] == candidates[idx - 1]:
                continue
            
            comb.append(candidates[idx])
            self.dfs(comb, combs, curr_target - candidates[idx], idx, candidates)
            comb.pop()
            


        

