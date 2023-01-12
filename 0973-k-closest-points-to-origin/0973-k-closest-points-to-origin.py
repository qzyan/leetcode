class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_points = sorted(points, key= lambda point: (self.calc_dist(point), point[0], point[1]))
        return sorted_points[:k]
            
            
    def calc_dist(self, point):
        return point[0] ** 2 + point[1] ** 2