class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums);
        
        n = len(nums) // 2
        
        total = 0
        for i in range(n):
            total += nums[i * 2]
            
        return total