class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right = 0, 0
        subarr_sum = 0
        length = float("inf")

        while right < len(nums):
            while left < right and subarr_sum >= target:
                curr_len = right - left
                if curr_len < length:
                    length = curr_len
                
                subarr_sum -= nums[left]
                left += 1

            subarr_sum += nums[right]
            right += 1

        while left < right and subarr_sum >= target:
            curr_len = right - left
            if curr_len < length:
                length = curr_len

            subarr_sum -= nums[left]
            left += 1

        return length if length != float("inf") else 0
