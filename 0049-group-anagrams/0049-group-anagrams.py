class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        CHARS = 'abcdefghijklmnopqrstuvwxyz'
        counts_str_mapping = {}
        
        for str in strs:
            char_count_mapping = {char: 0 for char in CHARS}
            for char in str:
                char_count_mapping[char] += 1
            
            counts_tuple = tuple(char_count_mapping.values())
            if counts_tuple in counts_str_mapping:
                counts_str_mapping[counts_tuple].append(str)
            else:
                counts_str_mapping[counts_tuple] = [str]
                
        anagrams = []
        for count, strs in counts_str_mapping.items():
            anagrams.append(strs)
            
        return anagrams