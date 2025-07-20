class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small_max_heap = [] # get the largest in 1st half
        large_min_heap = [] # get the smallest in 2nd half

        for i in range(k):
            heapq.heappush(small_max_heap, (-nums[i], i))

        for _ in range(k // 2):
            self.move(small_max_heap, large_min_heap)

        results = [self.get_median(small_max_heap, large_min_heap, k)]

        for i in range(k, len(nums)):
            idx_remove = i - k
            if not small_max_heap or nums[i] <= -small_max_heap[0][0]:
                heapq.heappush(small_max_heap, (-nums[i], i))
                if large_min_heap and nums[idx_remove] >= large_min_heap[0][0]:
                    self.move(small_max_heap, large_min_heap)
            else:
                heapq.heappush(large_min_heap, (nums[i], i))
                if small_max_heap and nums[idx_remove] <= -small_max_heap[0][0]:
                    self.move(large_min_heap, small_max_heap)

            while small_max_heap and small_max_heap[0][1] <= i - k:
                heapq.heappop(small_max_heap)
            while large_min_heap and large_min_heap[0][1] <= i - k:
                heapq.heappop(large_min_heap)

            results.append(self.get_median(small_max_heap, large_min_heap, k))

        return results

    def move(self, from_heap, to_heap):
        num, idx = heapq.heappop(from_heap)
        heapq.heappush(to_heap, (-num, idx))

    def get_median(self, small, large, k):
        if k % 2 == 1:
            num, idx = small[0]
            return -num

        num1, idx = small[0]
        num2, idx = large[0]

        return (num2 - num1) / 2
        
            
            