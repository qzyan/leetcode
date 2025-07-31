class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        paths = []
        self.dfs(path, paths, 0, 0, n)

        return paths

    def dfs(self, path, paths, open_count, close_count, n):
        if len(path) == n * 2:
            paths.append("".join(path))
            return

        if open_count < n:
            path.append("(")
            self.dfs(path, paths, open_count + 1, close_count, n)
            path.pop()

        if open_count > close_count:
            path.append(")")
            self.dfs(path, paths, open_count, close_count + 1, n)
            path.pop()           
        
