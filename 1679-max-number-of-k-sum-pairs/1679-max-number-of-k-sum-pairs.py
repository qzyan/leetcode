class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_of_operations = 0
        visited = {}
        for num in nums:
            comp = k - num
            if comp in visited and visited[comp] >= 1:
                count_of_operations += 1
                visited[comp] -= 1
            else:
                visited[num] = visited.get(num, 0) + 1
                
        return count_of_operations