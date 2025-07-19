class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # if max_h []: append to max_h
        # if num <= max_h max: append to max_h
        # if num > max_h max: append to min_h
        # rebalance
        max_h = self.max_heap
        min_h = self.min_heap
        if not max_h:
            heapq.heappush(max_h, -num)
            return

        if num <= -max_h[0]:
            heapq.heappush(max_h, -num)
        else:
            heapq.heappush(min_h, num)

        self.rebalance()

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2

        return float(-self.max_heap[0])
        
    def rebalance(self):
        # if len(max_h) < len(min_h): pop one from min_h and add to max_h
        # if len(max_h) + 1 > len(min_h): pop one from max_h and add to min_h
        max_h = self.max_heap
        min_h = self.min_heap

        if len(max_h) < len(min_h):
            num = heapq.heappop(min_h)
            heapq.heappush(max_h, -num)
            return

        if len(max_h) > len(min_h) + 1:
            num = heapq.heappop(max_h)
            num = -num
            heapq.heappush(min_h, num)
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()