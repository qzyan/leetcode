class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_char_counts = [0] * 26
        for char in p:
            p_char_counts[self.get_idx(char)] += 1
                
        s_char_counts = [0] * 26
        for idx in range(len(p)):
            char = s[idx]
            s_char_counts[self.get_idx(char)] += 1
        
        results = []
        if p_char_counts == s_char_counts:
            results.append(0)

        for idx in range(len(p), len(s)):
            prev_char = s[idx - len(p)]
            s_char_counts[self.get_idx(prev_char)] -= 1
            curr_char = s[idx]
            s_char_counts[self.get_idx(curr_char)] += 1
            
            if p_char_counts == s_char_counts:
                results.append(idx - len(p) + 1)

        return results

    def get_idx(self, char):
        return ord(char) - ord("a")