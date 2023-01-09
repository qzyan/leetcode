class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_cands = sorted(candidates)
        comb = []
        combs = []
        visited = [False] * len(sorted_cands)
        self.backtrack(comb, combs, sorted_cands, target, 0, visited)
        return combs
    
    def backtrack(self, comb, combs, sorted_cands, target, start_idx, visited):
        if target < 0:
            return
        
        if target == 0:
            combs.append(comb[:])
            return
        
        for idx in range(start_idx, len(sorted_cands)):
            if idx > 0 and sorted_cands[idx] == sorted_cands[idx - 1] and not visited[idx - 1]:
                continue
            
            visited[idx] = True
            comb.append(sorted_cands[idx])
            self.backtrack(comb, combs, sorted_cands, target - sorted_cands[idx], idx + 1, visited)
            visited[idx] = False
            comb.pop()