class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        paths = []
        self.dfs(candidates, target, path, paths, 0, 0)
        return paths

    def dfs(self, candidates, target, path, paths, start_idx, curr_total):
        if curr_total == target:
            paths.append(path[:])
            return
        
        if curr_total > target:
            return

        for idx in range(start_idx, len(candidates)):
            num = candidates[idx]
            path.append(num)
            self.dfs(candidates, target, path, paths, idx, curr_total + num)
            path.pop()