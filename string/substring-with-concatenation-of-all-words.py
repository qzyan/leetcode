class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        
        word_len = len(words[0])
        substring_len = word_len * len(words)
        words_freq_mapping = self.get_freq(words)
        results = []
        for start_idx in range(word_len):
            sub_results = self.find_substring_helper(s, start_idx, words_freq_mapping, word_len, substring_len)
            results += sub_results

        return results

    def find_substring_helper(self, s, start_idx, words_freq_mapping, word_len, substring_len):
        left = start_idx
        right = start_idx + word_len
        words_freq_of_s_mapping = {}
        results = []
        while right <= len(s):
            word = s[right - word_len:right]
            if word not in words_freq_mapping:
                left = right
                right = right + word_len
                words_freq_of_s_mapping = {}
                continue

            words_freq_of_s_mapping[word] = words_freq_of_s_mapping.get(word, 0) + 1
            while left < right and words_freq_of_s_mapping[word] > words_freq_mapping[word]:
                words_freq_of_s_mapping[s[left:left + word_len]] -= 1
                left += word_len
            
            if right - left == substring_len:
                results.append(left)
            
            right += word_len
        
        return results

    def get_freq(self, words):
        results = {}
        for word in words:
            results[word] = results.get(word, 0) + 1

        return results


            



