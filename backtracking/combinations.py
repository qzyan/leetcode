class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        paths = []
        
        self.dfs(path, paths, k, 1, n)

        return paths

    def dfs(self, path, paths, k, start_num, n):
        if len(path) == k:
            paths.append(path[:])
            return

        for i in range(start_num, n + 1):
            if n + 1 - i + len(path) < k:
                break

            path.append(i)
            self.dfs(path, paths, k, i + 1, n)
            path.pop()

        