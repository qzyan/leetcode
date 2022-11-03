import collections

class Solution:
    def numSquares(self, n: int) -> int:
        squares = set([i**2 for i in range(1, int(n**0.5) + 1)])
        queue = set()
        queue.add(n)
        depth = 0
        
        while queue:
            next_queue = set()
            for curr_remainder in queue:
                if curr_remainder in squares:
                    return depth + 1

                next_number = 1
                while next_number ** 2 <= curr_remainder:
                    next_remainder = curr_remainder - next_number ** 2
                    next_queue.add(next_remainder)
                    next_number += 1
                
            queue = next_queue
                
            depth += 1