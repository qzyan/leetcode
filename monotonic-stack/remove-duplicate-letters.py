class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        stack = []
        char_last_idx_mapping = self.get_char_last_idx_mapping(s)
        for idx in range(len(s)):
            char = s[idx]
            if char in visited:
                continue
            
            while stack and s[stack[-1]] > char and self.is_existing_after(s[stack[-1]], idx, char_last_idx_mapping):
                visited.remove(s[stack.pop()])
            
            stack.append(idx)
            visited.add(char)

        return "".join([ s[i] for i in stack])

    def is_existing_after(self, char, idx, char_last_idx_mapping):
        return char_last_idx_mapping[char] > idx

    def get_char_last_idx_mapping(self, s):
        mapping = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in mapping:
                mapping[s[i]] = i

        return mapping