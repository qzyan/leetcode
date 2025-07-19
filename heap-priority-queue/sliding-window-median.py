class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        results = []
        sortedlist = SortedList()
        left_idx = 0
        idx = 0
        nums_in_window = []
        while idx < k:
            num = nums[idx]
            sortedlist.add(num)
            idx += 1

        m = (sortedlist[len(sortedlist) // 2] + sortedlist[(len(sortedlist) - 1) // 2]) / 2
        results.append(m)
        while idx < len(nums):
            num = nums[idx]
            sortedlist.add(num)

            left_num = nums[left_idx]
            sortedlist.remove(left_num)

            m = (sortedlist[len(sortedlist) // 2] + sortedlist[(len(sortedlist) - 1) // 2]) / 2
            results.append(m)

            left_idx += 1
            idx += 1

        return results

    def insert(self, num, max_heap, min_heap):
        if not max_heap:
            heapq.heappush(max_heap, -num)
            return

        if num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) - 1 > len(min_heap):
            num = heapq.heappop(max_heap)
            num = -num
            heapq.heappush(min_heap, num)
        elif len(max_heap) < len(min_heap):
            num = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -num)

    def remove(self, num, max_heap, min_heap):
        if not max_heap:
            heapq.heappush(max_heap, -num)
            return

        if num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) - 1 > len(min_heap):
            num = heapq.heappop(max_heap)
            num = -num
            heapq.heappush(min_heap, num)
        elif len(max_heap) < len(min_heap):
            num = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -num)
    
    def get_median(self, max_heap, min_heap):
        if len(max_heap) == len(min_heap):
            return (heapq.heappop(min_heap) - heapq.heappop(max_heap)) / 2
        
        return float(-heapq.heappop(max_heap))
        
