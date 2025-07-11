class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            
            i = num
            while i in nums_set:
                i += 1
            
            res = max(res, i - num)

        return res