class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap to record the num - count
        # create a min heap
        # iterate over the each num - count
            # add the (count,num) to the heap
            # if the heap size larger than k
            # pop the ele with smallest freq count
        # return all the ele in heap 
        num_count_mapping = {}
        for num in nums:
            num_count_mapping[num] = num_count_mapping.get(num, 0) + 1
            
        heap = []
        for num, count in num_count_mapping.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return list(map(lambda ele: ele[1], heap))
            
            