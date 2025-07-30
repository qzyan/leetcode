class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        remove_count = 0
        for char in s:
            if char == "(":
                stack.append(char)
                continue
            
            # this ")" unmatched, should be removed
            if not stack:
                remove_count += 1
            else:
                stack.pop()

        remove_count += len(stack)
        return len(s) - remove_count