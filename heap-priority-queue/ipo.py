class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profits = []
        capital = capital[:]
        while k > 0:
            idxs = self.find_available_projects(capital, w)
            for idx in idxs:
                profit = profits[idx]
                heapq.heappush(max_profits, -profit)
            if max_profits:
                w -= heapq.heappop(max_profits)
            k -= 1
        
        return w

    def find_available_projects(self, capital, w):
        idxs = []
        for idx, c in enumerate(capital):
            if c <= w:
                idxs.append(idx)
                # mark it done
                capital[idx] = float("inf")

        return idxs