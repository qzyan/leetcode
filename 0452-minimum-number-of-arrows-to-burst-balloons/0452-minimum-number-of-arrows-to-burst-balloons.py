class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key = lambda x: x[1])
        count = 0
        last_end = None
        
        for point in points:
            if last_end is None:
                count += 1
                last_end = point[1]
                continue
                
            if point[0] > last_end:
                count += 1
                last_end = point[1]
            
        return count