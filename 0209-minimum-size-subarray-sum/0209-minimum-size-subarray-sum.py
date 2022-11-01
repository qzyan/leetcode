class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        if not nums or size == 0:
            return 0
        
        result = float("inf")
        
        sums = [0] * size
        curr_sum = 0
        for i in range(size):
            curr_sum += nums[i]
            sums[i] = curr_sum
            
        if curr_sum < target: 
            return 0
        
        if curr_sum == target:
            return size
        
        result = float('inf')
        
        for i in range(size):
            j = self.binary_search(sums, nums, i, size - 1, target)
            if j != -1:
                result = min(result, j - i + 1)
        
        return result if result <= size else 0
    
    def binary_search(self, sums, nums, low, high, target):
        start = low
        end = high
        
        while start < end:
            mid = (start + end) // 2
            if sums[mid] - sums[low] + nums[low] < target:
                start = mid + 1
            
            if sums[mid] - sums[low] + nums[low] >= target:
                end = mid
        
        if sums[start] - sums[low] + nums[low] < target:
            return -1 
        
        return start
                