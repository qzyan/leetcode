class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])

        step = 1
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return step

                for next_word in self.get_next_words(curr_word, word_set):
                    if next_word in visited:
                        continue

                    queue.append(next_word)
                    visited.add(next_word)    
            
            step += 1

        return 0

    def get_next_words(self, curr_word, word_set):
        next_words = []
        for idx in range(len(curr_word)):
            for char_idx in range(ord("a"), ord("z") + 1):
                char = chr(char_idx)

                if char == curr_word[idx]:
                    continue
                
                new_word = curr_word[:idx] + char + curr_word[idx + 1:]
                if new_word in word_set:
                    next_words.append(new_word)

        return next_words

