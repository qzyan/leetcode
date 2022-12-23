class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permut = []
        permuts = []
        visited = set()
        self.backtrack(permut, permuts, visited, nums, 0)
        return permuts
    
    def backtrack(self, permut, permuts, visited, nums, size):
        if size == len(nums):
            permuts.append(permut[:])
            return
        
        for num in nums:
            if num in visited:
                continue
                
            permut.append(num)
            visited.add(num)
            self.backtrack(permut, permuts, visited, nums, size + 1)
            visited.remove(num)
            permut.pop()
        