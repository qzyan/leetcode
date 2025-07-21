class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profits = []
        capital = [(cap, idx) for idx, cap in enumerate(capital)]
        heapq.heapify(capital)
        while k > 0:
            while capital and capital[0][0] <= w:
                cap, idx = heapq.heappop(capital)
                profit = profits[idx]
                heapq.heappush(max_profits, -profit)
            if max_profits:
                w -= heapq.heappop(max_profits)
            else:
                return w

            k -= 1
        
        return w