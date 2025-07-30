class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        unmatched_idxs = []
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                unmatched_idxs.append(idx)
                continue
            
            # char == ")"
            if unmatched_idxs and s[unmatched_idxs[-1]] == "(":
                unmatched_idxs.pop()
            else:
                unmatched_idxs.append(idx)

        prev_idx = -1
        longest_len = 0
        for idx in unmatched_idxs:
            longest_len = max(longest_len, idx - prev_idx - 1)
            prev_idx = idx

        longest_len = max(len(s) - prev_idx - 1, longest_len)

        return longest_len