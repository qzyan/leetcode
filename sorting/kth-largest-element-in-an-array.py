class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:]
        heapq.heapify(heap)
        result = 0
        for _ in range(len(nums) - k + 1):
            result = heapq.heappop(heap)
        
        return result