class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start, end):
        left, right = start, end
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        