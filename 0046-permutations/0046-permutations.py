class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = []
        is_visited = [False] * len(nums)
        self.dfs(nums, permutation, permutations, is_visited)
        
        
        return permutations
    
    def dfs(self, nums, permutation, permutations, is_visited):
        if len(permutation) == len(nums):
            permutations.append(permutation[:])
            return
        
        for idx, num in enumerate(nums):
            if is_visited[idx]:
                continue
            
            permutation.append(num)
            is_visited[idx] = True
            self.dfs(nums, permutation, permutations, is_visited)
            is_visited[idx] = False
            permutation.pop()
            
            