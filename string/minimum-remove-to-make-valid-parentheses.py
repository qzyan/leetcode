class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        chars = list(s)
        for i, char in enumerate(chars):
            if char == "(":
                stack.append(i)
            
            if char == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = ""

        for idx in stack:
            chars[idx] = ""

        return "".join(chars)