class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = [-1]
        max_len = 0
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                stack.append(idx)
                continue

            if stack:
                start_idx = stack.pop()
        
            if not stack:
                stack.append(idx)
        
            max_len = max(max_len, idx - stack[-1])

        return max_len