class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count

        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [] # keep the largest elements, remove smaller
        word_count_map = Counter(words)

        for word, count in word_count_map.items():
            heapq.heappush(heap, Element(count, word))
            if len(heap) > k:
                heapq.heappop(heap)

        sorted_elements = sorted(heap, key=lambda ele: (-ele.count, ele.word))
        return [ele.word for ele in sorted_elements]


