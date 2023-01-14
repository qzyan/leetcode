class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for start_num in nums:
            if start_num - 1 in nums_set:
                continue
            
            curr_len = 0
            curr_num = start_num
            while curr_num in nums_set:
                curr_len += 1
                curr_num += 1
                
            max_len = max(max_len, curr_len)
            
        return max_len