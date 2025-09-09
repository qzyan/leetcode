class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)

    def binary_search(self, nums, target):
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)
        
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] >= target:
            return left
        
        if nums[right] >= target:
            return right
        
        return len(nums)

        