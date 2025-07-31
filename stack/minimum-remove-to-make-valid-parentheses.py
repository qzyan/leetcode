class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""

        unmatched_idxs = []
        for idx in range(len(s)):
            char = s[idx]
            if char not in "()":
                continue
            
            if char == "(":
                unmatched_idxs.append(idx)
                continue
            
            if unmatched_idxs and s[unmatched_idxs[-1]] == "(":
                unmatched_idxs.pop()
            else:
                unmatched_idxs.append(idx)

        result = [char for char in s]
        for idx in unmatched_idxs:
            result[idx] = ""

        return "".join(result)