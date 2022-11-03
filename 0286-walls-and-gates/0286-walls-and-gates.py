import collections 
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row_size = len(rooms)
        col_size = len(rooms[0])
        gates = []
        for row_idx in range(row_size):
            for col_idx in range(col_size):
                if rooms[row_idx][col_idx] == 0:
                    gates.append((row_idx, col_idx))
                    
        self.calc_shortest_steps(rooms, gates)
                    
        return
    
    def calc_shortest_steps(self, rooms, gates):
        queue = collections.deque()
        visited = set()
        steps = 0
        
        for gate in gates:
            visited.add(gate)
            queue.append(gate)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                rooms[curr[0]][curr[1]] = steps
                
                for direction in DIRECTIONS:
                    next_position = ((curr[0] + direction[0]), (curr[1] + direction[1]))
                    if self.is_valid(next_position, rooms, visited):
                        visited.add(next_position)
                        queue.append(next_position)
                
            steps += 1
        
        return
        
    def is_valid(self, position, rooms, visited):
        row_idx, col_idx = position[0], position[1]
        if row_idx >= len(rooms) or row_idx < 0 or col_idx >= len(rooms[0]) or col_idx < 0:
            return False

        if rooms[row_idx][col_idx] == -1:
            return False
        
        if position in visited:
            return False 
        
        return True
                
                