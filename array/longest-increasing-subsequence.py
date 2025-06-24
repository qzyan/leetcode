class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp:
                dp.append(num)
                continue
            if num > dp[-1]:
                dp.append(num)
                continue

            idx = self.find_first_larger_or_equal(dp, num)
            if dp[idx] == num:
                continue
            
            dp[idx] = num

        return len(dp)

    def find_first_larger_or_equal(self, dp, target):
        left = 0
        right = len(dp) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if dp[mid] >= target:
                right = mid
            else:
                left = mid

        if dp[left] >= target:
            return left
        
        if dp[right] >= target:
            return right
        
        return len(dp)