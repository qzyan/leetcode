class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow, fast = 0, 0
        total = 0
        mini_len = float('inf');
        while fast < len(nums):
            while total < target and fast < len(nums):
                total += nums[fast]
                fast += 1
            
            if total < target:
                break
        
            while slow < fast and total >= target:
                total -= nums[slow]
                slow += 1

            mini_len = min(mini_len, fast - slow + 1)
            
        return mini_len if mini_len < float('inf') else 0
        