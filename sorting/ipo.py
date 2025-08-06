class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        c_ps = [(capital[idx], profits[idx]) for idx in range(n)]
        c_ps = sorted(c_ps) # [(c, p), ....]
        idx = 0
        max_heap = []
        while k > 0:
            # push all achievable projects in max_heap
            while idx < n and c_ps[idx][0] <= w:
                heapq.heappush(max_heap, (-c_ps[idx][1], c_ps[idx][0]))
                idx += 1

            if not max_heap:
                break
            
            # work on the most profitable project
            p, c = heapq.heappop(max_heap)
            p = -p
            w += p

            k -= 1

        return w
