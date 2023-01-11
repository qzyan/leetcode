import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        inheap = set([1])
        heapq.heapify(heap)
        curr_ugly = None
        
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            
            for factor in [2, 3, 5]:
                new_ugly = factor * curr_ugly
                if new_ugly in inheap:
                    continue
                heapq.heappush(heap, new_ugly)
                inheap.add(new_ugly)
                
        return curr_ugly
        
        