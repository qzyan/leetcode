class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        splited_words = self.split_arr(words, maxWidth)

        results = []
        for idx, words_arr in enumerate(splited_words):
            if len(words_arr) == 1:
                results.append(words_arr[0] + " " * (maxWidth - len(words_arr[0])))
                continue
            
            if idx == len(splited_words) - 1:
                result = " ".join(words_arr)
                result += (maxWidth - len(result)) * " "
                results.append(result)
                continue

            char_count = sum([len(w) for w in words_arr])
            space_count = maxWidth - char_count
            sep  = " " * (space_count // (len(words_arr) - 1))
            left_space_count = space_count % (len(words_arr) - 1)
            result = ""
            i = 0
            while i < len(words_arr) - 1:
                if i < left_space_count:
                    result += (words_arr[i] + sep + " ")
                else:
                    result += (words_arr[i] + sep)
                
                i += 1

            result += words_arr[-1]
            results.append(result)

        return results

    def split_arr(self, words, maxWidth):
        results = []
        result = []
        result_char_count = 0
        for word in words:
            if len(result) + result_char_count + len(word) > maxWidth:
                results.append(result)
                result = [word]
                result_char_count = len(word)
            else:
                result.append(word)
                result_char_count += len(word)
        
        results.append(result)

        return results