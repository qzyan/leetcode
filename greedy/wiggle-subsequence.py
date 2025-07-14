class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        is_pos = [False] * len(nums)

        max_len = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[0]:
                dp[idx] = 2
                if nums[idx] > nums[0]:
                    is_pos[idx] = True

            for j in range(1, idx):
                if (is_pos[j] and nums[idx] < nums[j]) or (not is_pos[j] and nums[idx] > nums[j]):
                    if dp[idx] < dp[j] + 1:
                        dp[idx] = dp[j] + 1
                        is_pos[idx] = nums[idx] > nums[j]

            max_len = max(max_len, dp[idx])

        return max_len
