class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # iterate over each ele from the back, find the first ele that nums[i] < nums[i + 1]
        # iterate over each ele from nums[i + 1], find the smallest ele that is larger than nums[i] -> nums[j]
        # swap nums[i] and nums[j]
        # reverse the nums[i + 1 :]
        
        
        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] < nums[idx + 1]:
                first_idx = idx
                break
        else:
            self.reverse_arr(nums, 0, len(nums) - 1)
            return
        
        for idx in range(first_idx + 1, len(nums)):
            if nums[idx] <= nums[first_idx]:
                second_idx = idx - 1
                break
        else:
            second_idx = len(nums) - 1
            
        nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
        
        start = first_idx + 1
        end = len(nums) - 1
        self.reverse_arr(nums, start, end)
        
        return
            
    def reverse_arr(self, nums, start, end):
        left = start
        right = end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
            
        
        