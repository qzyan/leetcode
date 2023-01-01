class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        char_word_dict = {}
        word_char_dict = {}
        for idx, char in enumerate(pattern):
            word = words[idx]
            if char in char_word_dict and word in word_char_dict:
                if char_word_dict[char] != word or word_char_dict[word] != char:
                    return False
            elif char not in char_word_dict and word not in word_char_dict:
                char_word_dict[char] = word
                word_char_dict[word] = char
            else:
                return False
                
        
        return True
                
            