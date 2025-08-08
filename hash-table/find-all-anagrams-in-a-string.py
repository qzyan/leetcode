class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_char_counts = [0] * 26
        for char in p:
            p_char_counts[ord(char) - ord("a")] += 1
        
        p_code = self.get_code(p_char_counts)
        
        s_char_counts = [0] * 26
        for idx in range(len(p)):
            s_char_counts[ord(s[idx]) - ord("a")] += 1
        
        results = []
        s_code = self.get_code(s_char_counts)
        if p_code == s_code:
            results.append(0)

        for idx in range(len(p), len(s)):
            prev_char = s[idx - len(p)]
            s_char_counts[ord(prev_char) - ord("a")] -= 1
            curr_char = s[idx]
            s_char_counts[ord(curr_char) - ord("a")] += 1
            
            s_code = self.get_code(s_char_counts)
            if p_code == s_code:
                results.append(idx - len(p) + 1)

        return results


    def get_code(self, char_counts):
        return "".join([str(count) for count in char_counts])