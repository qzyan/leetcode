class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums = sorted(nums)
        permut = []
        permuts = []
        visited = [False] * len(nums)
        
        self.backtrack(permut, permuts, nums, visited)
        
        return permuts
        
    def backtrack(self, permut, permuts, nums, visited):
            if len(permut) == len(nums):
                permuts.append(permut[:])
                return
            
            for idx, num in enumerate(nums):
                if visited[idx]:
                    continue
                    
                if idx > 0 and num == nums[idx - 1] and \
                   not visited[idx - 1]:
                    continue
                    
                visited[idx] = True
                permut.append(num)
                self.backtrack(permut, permuts, nums, visited)
                permut.pop()
                visited[idx] = False
                
                    
                    