class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        # collect the unmatched idxs
        # can only be ))))(((
        stack = []
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                stack.append(idx)
                continue

            # char == ")"
            # there is ( to match
            if stack and s[stack[-1]] == "(":
                stack.pop()
            # no "(" to match
            else:
                stack.append(idx)

        prev_idx = -1
        max_len = 0
        for idx in stack:
            max_len = max(max_len, idx - prev_idx - 1)
            prev_idx = idx

        max_len = max(max_len, len(s) - prev_idx - 1)

        return max_len

