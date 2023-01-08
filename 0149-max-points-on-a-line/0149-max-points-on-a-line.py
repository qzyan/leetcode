class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        if len(points) == 1:
            return 1
        
        max_count = 2
        
        for idx_point1, point1 in enumerate(points):
            slopes = {}
            for idx_point2 in range(idx_point1 + 1, len(points)):
                point2 = points[idx_point2]
                slope = self.calc_slope(point1, point2)
                slopes[slope] = slopes.get(slope, 1) + 1
                max_count = max(max_count, slopes[slope])
            
        return max_count
    
    def calc_slope(self, point1, point2):
        return (point1[1] - point2[1]) / (point1[0] - point2[0]) if point1[0] != point2[0] else float('inf')