class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []
        word_count = Counter(words)

        results = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

        return [word for word, _ in results[:k]]