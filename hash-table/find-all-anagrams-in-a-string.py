class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_code = self.encode(p)

        char_count = [0] * 26
        for i in range(len(p)):
            char = s[i]
            char_count[ord(char) - ord("a")] += 1

        results = []
        for start_idx in range(len(s) - len(p) + 1):
            s_code = tuple(char_count)
            if s_code == p_code:
                results.append(start_idx)

            if start_idx == len(s) - len(p):
                break

            char_count[ord(s[start_idx]) - ord("a")] -= 1
            char_count[ord(s[start_idx + len(p)]) - ord("a")] += 1
            start_idx += 1

        return results

    def encode(self, p):
        char_count = [0] * 26
        for char in p:
            char_count[ord(char) - ord("a")] += 1

        return tuple(char_count)