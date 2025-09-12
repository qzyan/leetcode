class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[-1] and target <= nums[-1] or nums[mid] > nums[-1] and target > nums[-1]:
                if target < nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] <= nums[-1] and target > nums[-1]:
                right = mid
            else:
                left = mid
        
        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right

        return -1
            
            
