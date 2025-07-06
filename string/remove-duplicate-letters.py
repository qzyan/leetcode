class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        char_last_idx = self.get_last_idx(s)
        for idx in range(len(s)):
            char = s[idx]
            if char in visited:
                continue

            while stack:
                last_char_in_stack = s[stack[-1]]
                if last_char_in_stack > char and self.exists_after(last_char_in_stack, idx, char_last_idx):
                    stack.pop()
                    visited.remove(last_char_in_stack)
                else:
                    break
            
            stack.append(idx)
            visited.add(char)

        return "".join([s[idx] for idx in stack])

    def get_last_idx(self, s):
        results = {}
        for idx in range(len(s) - 1, -1, -1):
            char = s[idx]
            if char in results:
                continue

            results[char] = idx

        return results

    def exists_after(self, char, idx, char_last_idx):
        return char_last_idx[char] > idx

    