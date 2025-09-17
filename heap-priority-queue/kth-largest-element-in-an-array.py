class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k, 0, len(nums) - 1)

    def quick_select(self, nums, k, start, end):
        pivot = (nums[(start + end) // 2])
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1

            while left <= right and nums[right] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if start + k - 1 <= right:
            return self.quick_select(nums, k, start, right)
        
        if start + k - 1 >= left:
            return self.quick_select(nums, k - (left - start), left, end)
        
        return nums[start + k - 1]
                 
