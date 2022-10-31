class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0 or not nums:
            return 0
        
        left_sum = 0
        right_sum = 0
        
        for i in range(1, len(nums)):
            right_sum += nums[i]
            
        if left_sum == right_sum:
            return 0
        
        for curr_index in range(1, len(nums)):
            left_sum += nums[curr_index - 1]
            right_sum -= nums[curr_index]
            
            if left_sum == right_sum:
                return curr_index
            
        return -1