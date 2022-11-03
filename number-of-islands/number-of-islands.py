import collections

DIRECTIONS = ((0, 1),(0, -1),(-1, 0),(1, 0))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row_size = len(grid)
        col_size = len(grid[0])
        
        visited = [[False] * col_size for _ in range(row_size)] 
        count = 0
        
        for row_idx in range(row_size):
            for col_idx in range(col_size):
                if grid[row_idx][col_idx] == "1" and not visited[row_idx][col_idx]:
                    self.bfs_all_adjacent_islands(grid, visited, row_idx, col_idx)
                    count += 1
        
        
        return count
    
    def bfs_all_adjacent_islands(self, grid, visited, row_idx, col_idx):
        queue = collections.deque()
        visited[row_idx][col_idx] = True
        queue.append((row_idx, col_idx))
        
        while queue:
            curr_row, curr_col = queue.popleft()
            
            for direction in DIRECTIONS:
                next_row = curr_row + direction[0]
                next_col = curr_col + direction[1]
                if self.is_valid_position(grid, visited, next_row, next_col):
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
        
        return 
        
    def is_valid_position(self, grid, visited, row, col):
        row_size = len(grid)
        col_size = len(grid[0])


        if row < 0 or row >= row_size or col < 0 or col >= col_size:
            return False
        
        if visited[row][col]:
            return False
        

        if grid[row][col] == "0":
            return False 
        print(row, col)
        return True
        
        
        
        
        
        
        