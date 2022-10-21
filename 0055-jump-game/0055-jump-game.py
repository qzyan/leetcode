
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
# dp using the current reachable state to get the reachable state of later 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        
        is_reachable = [False for _ in range(len(nums))]
        is_reachable[0] = True
        
        for (index, num) in enumerate(nums):
            if not is_reachable[index]:
                return False
            
            for step in range(1, num + 1):
                if index + step < len(is_reachable) and is_reachable[index + step]:
                    continue
                if index + step < len(is_reachable):
                    is_reachable[index + step] = True
            
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