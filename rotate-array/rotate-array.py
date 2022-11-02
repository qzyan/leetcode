class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        
        nums.reverse()
        
        self.reverse_sub_list(nums, 0, k - 1)
        self.reverse_sub_list(nums, k, size - 1)
            
        return
    
    def reverse_sub_list(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            