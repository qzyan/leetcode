class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or dp[-1] < num:
                dp.append(num)
                continue
            
            idx = self.first_larger_or_equal(dp, num)
            dp[idx] = num

        return len(dp)
    
    def first_larger_or_equal(self, nums, target):
        if target > nums[-1]:
            return len(nums)
        
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] >= target:
            return left
        
        if nums[right] >= target:
            return right
        
        return len(nums)