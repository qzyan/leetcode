class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.encode(s) == self.encode(t)

    def encode(self, s):
        code = [0] * 26

        for char in s:
            idx = ord(char) - ord("a")
            code[idx] += 1

        return "".join([str(c) for c in code])