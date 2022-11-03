import collections

class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.capacity = size
        self.count = 0
        self.total = 0

    def next(self, val: int) -> float:
        if self.count == self.capacity:
            poped = self.queue.popleft()
            self.total -= poped
            self.count -= 1
            
        self.queue.append(val)
        self.total += val
        self.count += 1
        
        return self.total / self.count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)