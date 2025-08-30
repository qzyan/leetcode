class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        visited_idxs = set()
        path = []
        paths = []
        self.dfs(nums, visited_idxs, path, paths)
        return paths

    def dfs(self, nums, visited_idxs, path, paths):
        if len(path) == len(nums):
            paths.append(path[:])
            return

        for idx, num in enumerate(nums):
            if idx in visited_idxs:
                continue
            
            if idx > 0 and nums[idx] == nums[idx - 1] and idx - 1  not in visited_idxs:
                continue
            
            path.append(num)
            visited_idxs.add(idx)
            self.dfs(nums, visited_idxs, path, paths)
            visited_idxs.remove(idx)
            path.pop()