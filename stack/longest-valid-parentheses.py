class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                stack.append(idx)
                continue
            
            # char == ")"
            if stack:
                stack.pop()
            if not stack:
                stack.append(idx)
                continue
            
            max_len = max(max_len, idx - stack[-1])

        return max_len


