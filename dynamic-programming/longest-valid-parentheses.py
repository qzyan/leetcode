class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        # collect the unmatched idxs
        # can only be ))))(((
        stack = []
        max_len = 0
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                stack.append(idx)
                continue

            # char == ")"
            # there is ( to match
            if stack and s[stack[-1]] == "(":
                stack.pop()
                prev_idx = stack[-1] if stack else -1
                max_len = max(max_len, idx - prev_idx)
            # no "(" to match
            else:
                stack.append(idx)

        return max_len
