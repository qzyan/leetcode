class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count_mapping = {}
        for char in s:
            char_count_mapping[char] = char_count_mapping.get(char, 0) + 1
        
        for idx, char in enumerate(s):
            if char_count_mapping[char] == 1:
                return idx
        return -1