class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        res = 1
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            
            i = num + 1
            while i in nums_set:
                res = max(res, i - num + 1)
                i += 1

        return res