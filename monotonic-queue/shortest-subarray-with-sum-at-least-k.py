class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        left = 0
        right = 0
        sum_val = 0
        length = float("inf")
        while right < len(nums):
            sum_val += nums[right]
            right += 1

            while left < right and sum_val >= k:
                if right - left < length:
                    length = right - left
                
                sum_val -= nums[left]
                left += 1

        return length if length != float("inf") else -1

            