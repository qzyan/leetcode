class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []

        word_count = self.count_words(words)
        
        # [("word", 5)]
        items = list(word_count.items())
        items.sort(key=lambda x: (-x[1], x[0]))

        return [item[0] for item in items[:k]]

    def count_words(self, words):
        mapping = {}
        for word in words:
            mapping[word] = mapping.get(word, 0) + 1

        return mapping

        