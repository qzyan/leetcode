class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        min_heap = []
        for word, count in word_count.items():
            ele = Element(word, count)
            heapq.heappush(min_heap, ele)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        results = []
        while min_heap:
            word = heapq.heappop(min_heap).word
            results.append(word)

        results.reverse()
        return results

class Element:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        
        return other.word < self.word