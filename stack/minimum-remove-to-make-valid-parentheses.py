class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s

        unmatched_idxs = []

        for idx in range(len(s)):
            char = s[idx]
            if char not in "()":
                continue
            
            if char == "(":
                unmatched_idxs.append(idx)
            else:
                if unmatched_idxs and s[unmatched_idxs[-1]] == "(":
                    unmatched_idxs.pop()
                else:
                    unmatched_idxs.append(idx)

        chars = [char for char in s]
        for idx in unmatched_idxs:
            chars[idx] = ""

        return "".join(chars)