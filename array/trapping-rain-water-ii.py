class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        
        heap_queue = []
        visited = set()
        self.add_all_boarders(heightMap, heap_queue, visited)
        water = 0
        water_level = 0
        while heap_queue:
            curr_grid_height, curr_row, curr_col = heapq.heappop(heap_queue)
            if curr_grid_height > water_level:
                water_level = curr_grid_height
            else:
                water += water_level - curr_grid_height
            
            for neighbor in self.get_neighbors(heightMap, curr_row, curr_col):
                if neighbor in visited:
                    continue
                
                next_row, next_col = neighbor
                visited.add(neighbor)
                heapq.heappush(heap_queue, (heightMap[next_row][next_col], next_row, next_col))

        return water
    
    def add_all_boarders(self, heightMap, heap_queue, visited):
        for row in range(len(heightMap)):
            heapq.heappush(heap_queue, (heightMap[row][0], row, 0))
            visited.add((row, 0))

            heapq.heappush(heap_queue, (heightMap[row][len(heightMap[0]) - 1], row, 0))
            visited.add((row, len(heightMap[0]) - 1))

        for col in range(1, len(heightMap[0]) - 1):
            heapq.heappush(heap_queue, (heightMap[0][col], 0, col))
            visited.add((0, col))

            heapq.heappush(heap_queue, (heightMap[len(heightMap) - 1][col], len(heightMap) - 1, col))
            visited.add((len(heightMap) - 1, col))


    def get_neighbors(self, heightMap, row, col):
        neighbors = []
        for d_row, d_col in DIRECTIONS:
            next_row = d_row + row
            next_col = d_col + col

            if 0 <= next_row < len(heightMap) and 0 <= next_col < len(heightMap[0]):
                neighbors.append((next_row, next_col))

        return neighbors

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]