class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m == 0:
            return (nums2[n // 2] + nums2[(n - 1)// 2]) / 2
        if n == 0:
            return (nums1[m // 2] + nums1[(m - 1)// 2]) / 2

        return (self.find_idx(nums1, nums2, (m + n) // 2) + self.find_idx(nums1, nums2, (m + n - 1) // 2)) / 2

    def find_idx(self, nums1, nums2, idx):
        left = min(nums1[0], nums2[0])
        right = max(nums1[-1], nums2[-1])

        while left + 1 < right:
            num = (left + right) // 2
            # first idx that nums[idx] >= num
            idx1 = self.binary_search(nums1, num)
            idx2 = self.binary_search(nums2, num)

            if idx1 + idx2 <= idx:
                left = num
            else:
                right = num

        if self.binary_search(nums1, right) + self.binary_search(nums2, right) == idx:
            return right

        return left

    def binary_search(self, nums, num):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= num:
                right = mid
            else:
                left = mid

        if nums[left] >= num:
            return left
        
        if nums[right] >= num:
            return right

        return len(nums)
        
