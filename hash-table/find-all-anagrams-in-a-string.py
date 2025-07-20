class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        p_count = [0] * 26
        for char in p:
            idx = ord(char) - ord("a")
            p_count[idx] += 1

        s_count = [0] * 26
        
        for idx in range(len(p)):
            char = s[idx]
            s_count[ord(char) - ord("a")] += 1

        p_code = tuple(p_count)
        s_code = tuple(s_count)
        results = []
        if p_code == s_code:
            results.append(0)

        for idx in range(len(p), len(s)):
            char_add = s[idx]
            char_remove = s[idx - len(p)]
            s_count[ord(char_add) - ord("a")] += 1
            s_count[ord(char_remove) - ord("a")] -= 1

            s_code = tuple(s_count)
            if p_code == s_code:
                results.append(idx - len(p) + 1)

        return results

        

