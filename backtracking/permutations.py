class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        path, paths = [], []
        self.dfs(nums, visited, path, paths)
        return paths

    def dfs(self, nums, visited, path, paths):
        if len(path) == len(nums):
            paths.append(path[:])
            return

        for num in nums:
            if num in visited:
                continue
            
            path.append(num)
            visited.add(num)
            self.dfs(nums, visited, path, paths)
            visited.remove(num)
            path.pop()

        