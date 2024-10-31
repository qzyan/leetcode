class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        visited = dict();
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in visited:
                return [i, visited[needed]]
            else:
                visited[nums[i]] = i
                
        return [-1, -1]
            