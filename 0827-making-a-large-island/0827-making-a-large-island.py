import collections

class GridType:
    Water = 0
    Island = 1
    
DIRECTIONS = ((1, 0), (-1, 0), (0, -1), (0, 1))

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        areas = [[(0, 0) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        print(areas)
        max_area = 0
        island_cluster_no = 1
        visited = set()
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == GridType.Water:
                    continue
                if (row_idx, col_idx) in visited:
                    continue
                
                visited.add((row_idx, col_idx))
                islands, area = self.bfs(grid, row_idx, col_idx, visited)
                self.mark_area(islands, area, areas, island_cluster_no)
                island_cluster_no += 1
                max_area = max(area, max_area)
                
        for row_idx in range(len(areas)):
            for col_idx in range(len(areas[0])):
                island_no = areas[row_idx][col_idx][0]
                area = areas[row_idx][col_idx][1]
                
                if area != 0:
                    continue
                
                area = 1
                prev_island_nos = set()
                neighbors = self.get_neighbors(grid, (row_idx, col_idx))
                for neighbor_row, neighbor_col in neighbors:
                    neighbor_island_no, neighbor_area = areas[neighbor_row][neighbor_col]
                    if neighbor_island_no not in prev_island_nos:
                        area += neighbor_area
                        prev_island_nos.add(neighbor_island_no)
                max_area = max(area, max_area)

        return max_area
    
    
    def bfs(self, grid, row_ori, col_ori, visited):
        boundaries = set()
        area = 0
        islands = []
        queue = collections.deque()
        queue.append((row_ori, col_ori))
        visited.add((row_ori, col_ori))
        
        while queue:
            curr = queue.popleft()
            area += 1
            islands.append(curr)
            
            neighbors = self.get_neighbors(grid, curr)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                
                visited.add(neighbor)
                queue.append(neighbor)

        return islands, area
    
    def get_neighbors(self, grid, curr):
        neighbors = []
        for d_row, d_col in DIRECTIONS:
            next_row = curr[0] + d_row
            next_col = curr[1] + d_col
            next_cell = (next_row, next_col)
            
            if self.is_inbound(grid, next_cell) and grid[next_row][next_col] == GridType.Island:
                neighbors.append(next_cell)
        
        return neighbors
    
    def is_inbound(self, grid, cell):
        return 0 <= cell[0] < len(grid) and 0 <= cell[1] < len(grid[0])
    
    def mark_area(self, islands, area, areas, island_cluster_no):
        for island in islands:
            areas[island[0]][island[1]] = (island_cluster_no, area)