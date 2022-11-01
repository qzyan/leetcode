class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        size = len(nums)
        
        result = float("inf")
        
        left, right = 0, 0
        sum_left_right = 0
        
        while right < size:
            sum_left_right += nums[right]
            
            while sum_left_right >= target:
                result = min(result, right - left + 1)
                sum_left_right -= nums[left]
                left += 1
            
            right += 1
            
            
        return result if result != float("inf") else 0
                