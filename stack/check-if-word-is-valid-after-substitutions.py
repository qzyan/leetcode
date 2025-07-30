class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "a":
                stack.append("a")
            elif char == "b":
                stack.append("b")
            elif char == "c":
                for prev_char in "ba":
                    if not stack:
                        return False
                    if stack.pop() != prev_char:
                        return False
            else:
                return False

        return len(stack) == 0