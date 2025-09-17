class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profit = []
        for idx in range(len(capital)):
            capital_profit.append((capital[idx], profits[idx]))

        capital_profit.sort()

        max_profit_heap = []
        idx = 0
        for _ in range(k):
            while idx < len(capital_profit) and capital_profit[idx][0] <= w:
                heapq.heappush(max_profit_heap, -capital_profit[idx][1])
                idx += 1
            
            if max_profit_heap:
                profit = -heapq.heappop(max_profit_heap)
                w += profit

        return w
