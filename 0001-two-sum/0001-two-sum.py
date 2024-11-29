class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {};
        for i in range(len(nums)):
            num_a = nums[i]
            num_b = target - num_a
            
            if num_b in mapping:
                return (mapping[num_b], i)
            
            mapping[num_a] = i
            
        return [-1, -1]
        