class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        start_idx = self.find_start_idx(nums, target)
        end_idx = self.find_end_idx(nums, target)
        return [start_idx, end_idx]

    def find_start_idx(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            num = nums[mid]
            if num >= target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right

        return -1

    def find_end_idx(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            num = nums[mid]
            if num <= target:
                left = mid
            else:
                right = mid

        if nums[right] == target:
            return right
        
        if nums[left] == target:
            return left

        return -1
