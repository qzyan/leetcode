class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        idx = 0
        max_heap = []
        min_heap = []
        for idx in range(n):
            heapq.heappush(min_heap, (capital[idx], idx))
        while k > 0:
            # push all achievable projects in max_heap
            while min_heap and min_heap[0][0] <= w:
                c, idx = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-profits[idx]))

            if not max_heap:
                break
            
            # work on the most profitable project
            p = heapq.heappop(max_heap)
            p = -p
            w += p

            k -= 1

        return w
