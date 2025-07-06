class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_set = set(t)
        t_char_count_mapping = self.get_char_count(t)
        s_valid_char_count_mapping = {}
        valid_char_in_s_count = 0
        slow, fast = 0, 0
        min_len = float("inf")
        l, r = 0, 0
        while fast < len(s):
            char = s[fast]
            if char not in t_set:
                fast += 1
                continue
            
            s_valid_char_count_mapping[char] = s_valid_char_count_mapping.get(char, 0) + 1
            if s_valid_char_count_mapping[char] == t_char_count_mapping[char]:
                valid_char_in_s_count += 1
            
            if valid_char_in_s_count < len(t_set):
                fast += 1
                continue

            while s[slow] not in t_set or s_valid_char_count_mapping[s[slow]] > t_char_count_mapping[s[slow]]:
                if s[slow] not in t_set:
                    slow += 1
                    continue
                
                s_valid_char_count_mapping[s[slow]] -= 1
                slow += 1
            
            if fast - slow + 1 < min_len:
                l = slow
                r = fast
                min_len = fast - slow + 1
            
            fast += 1
        
        return s[l:r + 1] if min_len != float("inf") else ""

    def get_char_count(self, s):
        results = {}
        for char in s:
            results[char] = results.get(char, 0) + 1

        return results
            
