class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.k_sum_closest(nums, 0, target, 3)
    
    def k_sum_closest(self, nums, start_idx, target, k):
        if k == 2:
            return self.two_sum_closest(nums, start_idx, target)
        
        closest = float('inf')
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx - 1] == num:
                continue
            if idx + k > len(nums):
                break
            next_closest = self.k_sum_closest(nums, idx + 1,target - num, k - 1)
            if abs(num + next_closest - target) < abs(closest - target):
                closest = num + next_closest
        
        return closest
    
    def two_sum_closest(self, nums, start_idx, target):
        left = start_idx
        right = len(nums) - 1
        closest = float('inf')
        
        while left < right:
            total = nums[left] + nums[right]
            
            if abs(total - target) < abs(closest - target):
                closest = total 
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return target
        
        return closest
        