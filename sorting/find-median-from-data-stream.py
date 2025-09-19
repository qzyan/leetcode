class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return
        
        if -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        self.rebalance()

    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)
            return
        
        if len(self.max_heap) < len(self.min_heap):
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if not self.max_heap and not self.min_heap:
            return 0.0

        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return float(-self.max_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()