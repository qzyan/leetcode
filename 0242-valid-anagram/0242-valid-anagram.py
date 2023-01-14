class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_mapping = {}
        for char in s:
            char_count_mapping[char] = char_count_mapping.get(char, 0) + 1
        
        for char in t:
            if char not in char_count_mapping:
                return False
            
            char_count_mapping[char] = char_count_mapping.get(char) - 1
            
        for char, count in char_count_mapping.items():
            if count != 0:
                return False
        
        return True