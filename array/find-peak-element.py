class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if self.is_asc(nums, mid):
                left = mid
            else:
                right = mid
        
        return left if nums[left] > nums[right] else right
    
    def is_asc(self, nums, idx):
        if idx == 0:
            return True
        
        return nums[idx] > nums[idx - 1]