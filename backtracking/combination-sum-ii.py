class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        comb = []
        combs = []
        self.dfs(comb, combs, nums, target, 0, 0, set())

        return combs

    def dfs(self, comb, combs, nums, target, curr_sum, start_idx, visited):
        if curr_sum == target:
            combs.append(comb[:])
            return
        
        if curr_sum > target:
            return
        
        for idx in range(start_idx, len(nums)):
            if idx - 1 >= 0 and nums[idx] == nums[idx - 1] and idx - 1 not in visited:
                continue
            
            comb.append(nums[idx])
            visited.add(idx)
            self.dfs(comb, combs, nums, target, curr_sum + nums[idx], idx + 1, visited)
            visited.remove(idx)
            comb.pop()