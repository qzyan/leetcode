class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        fast = 0
        total = 0
        min_size = float("inf")
        while fast < len(nums):
            total += nums[fast]
    
            while total >= target and slow <= fast:
                min_size = min(min_size, fast - slow + 1)
                total -= nums[slow]
                slow += 1
    
            fast += 1

        return min_size if min_size != float("inf") else 0