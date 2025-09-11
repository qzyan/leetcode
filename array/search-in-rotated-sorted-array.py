class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotated_idx = self.find_rotated_idx(nums)
        idx = self.binary_search(nums, 0, rotated_idx - 1, target)
        if idx != -1:
            return idx
        return self.binary_search(nums, rotated_idx, len(nums) - 1, target)

    def find_rotated_idx(self, nums):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid
        
        return left if nums[left] < nums[right] else right

    def binary_search(self, nums, left, right, target):
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        
        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right

        return -1
