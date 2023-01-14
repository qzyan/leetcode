class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = {}
        recorder = {'longest_len': 0}
        nums_set = set(nums)
        for start_ele in nums:
            self.dfs(start_ele, memo, recorder, nums_set)
        
        return recorder['longest_len']
            
    def dfs(self, start_ele, memo, recorder, nums_set):
        if start_ele in memo:
            return memo[start_ele]
        
        next_num = start_ele + 1
        if next_num in nums_set:            
            memo[start_ele] = self.dfs(next_num, memo, recorder, nums_set) + 1
        else:
            memo[start_ele] = 1
            
        recorder['longest_len'] = max(recorder['longest_len'], memo[start_ele])
        
        return memo[start_ele]    
        