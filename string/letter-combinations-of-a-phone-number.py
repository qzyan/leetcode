class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        path = []
        paths = []
        self.dfs(digits, 0, path, paths, digit_chars)
        return paths

    def dfs(self, digits, curr_idx, path, paths, digit_chars):
        if curr_idx == len(digits):
            paths.append("".join(path))
            return

        digit = digits[curr_idx]
        for char in digit_chars[digit]:
            path.append(char)
            self.dfs(digits, curr_idx + 1, path, paths, digit_chars)
            path.pop()