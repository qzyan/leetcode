# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        
        right_most_index = 0
        for index in range(len(nums)):
            if index > right_most_index:
                return False 
            
            right_most_index = max(right_most_index, index + nums[index])
            
            if right_most_index >= len(nums) - 1:
                return True
        
        return False
                

"""
# dp using the current reachable state to get the reachable state of later 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        
        is_reachable = [False for _ in range(len(nums))]
        is_reachable[0] = True
        
        for index in range(len(nums)):
            if not is_reachable[index]:
                return False
            
            max_step = nums[index]
            for step in range(1, max_step + 1):
                if index + step >= len(is_reachable):
                    break
                if is_reachable[index + step]:
                    continue
                
                is_reachable[index + step] = True
                
                if is_reachable[-1]:
                    return True
        return True
"""


"""
# dp using the previous reachable state to get the current reachable state 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        
        is_reachable = [False for _ in range(len(nums))]
        is_reachable[0] = True
        
        for index in range(len(nums)):
            for prev_index in range(index - 1, -1, -1):
                if prev_index + nums[prev_index] >= index:
                    is_reachable[index] = True
                    break
            
            if not is_reachable[index]:
                return False
        
        return is_reachable[-1]
"""

"""
# dfs
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        
        # special cases
        if nums is None or len(nums) == 0:
            return False
        
        return self.dfs(nums, 0)
    
    def dfs(self, nums, curr_index):
        if curr_index == len(nums) - 1:
            return True
        
        max_step = nums[curr_index]
        for next_index in range(curr_index + 1, curr_index + 1 + max_step):
            if self.dfs(nums, next_index):
                return True
        
        return False
"""