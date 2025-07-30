class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        # record all unmatched (, ) idxs
        unmatched_idxs = []
        longest_len = 0
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                prev_unmatched_idx = unmatched_idxs[-1] if unmatched_idxs else -1
                longest_len = max(longest_len, idx - prev_unmatched_idx - 1)
                unmatched_idxs.append(idx)
                continue
            
            # char == ")"
            if unmatched_idxs and s[unmatched_idxs[-1]] == "(":
                unmatched_idxs.pop()
            else:
                prev_unmatched_idx = unmatched_idxs[-1] if unmatched_idxs else -1
                longest_len = max(longest_len, idx - prev_unmatched_idx - 1)
                prev_idx = idx
                unmatched_idxs.append(idx)

        prev_unmatched_idx = unmatched_idxs[-1] if unmatched_idxs else -1
        longest_len = max(len(s) - prev_unmatched_idx - 1, longest_len)

        return longest_len