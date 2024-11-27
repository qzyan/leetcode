class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        if sum(nums) < target:
            return 0
        
        left = 1
        right = len(nums)
        
        while left + 1 < right:
            mid = (left + right) //2 
            if self.has_subarray_larger_than_target(target, nums, mid):
                right = mid
            else:
                left = mid
        
        if self.has_subarray_larger_than_target(target, nums, left):
            return left
        
        if self.has_subarray_larger_than_target(target, nums, right):
            return right
        
        return 0
    
    def has_subarray_larger_than_target(self, target, nums, length):
        total = 0
        right = 0
        left = 0
        
        while right < length:
            total += nums[right]
            right += 1
        
        if total >= target:
            return True
        
        while right < len(nums):                        
            total += nums[right]
            total -= nums[left]
            right +=1
            left += 1
            
            if total >= target:
                return True
                
        return False
            