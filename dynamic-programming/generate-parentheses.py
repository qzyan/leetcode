class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        paths = []
        self.dfs(path, paths, 0, 0, n)

        return paths

    def dfs(self, path, paths, forward_count, backward_count, n):
        if forward_count == n and backward_count == n:
            paths.append("".join(path))
            return

        if forward_count < n:
            path.append("(")
            self.dfs(path, paths, forward_count + 1, backward_count, n)
            path.pop()

        if backward_count < forward_count:
            path.append(")")
            self.dfs(path, paths, forward_count, backward_count + 1, n)
            path.pop()

        return

