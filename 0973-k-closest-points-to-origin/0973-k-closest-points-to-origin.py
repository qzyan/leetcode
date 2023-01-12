import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            dist = self.calc_dist(point)
            heapq.heappush(heap, (-dist, -point[0], -point[1]))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        
        return map(lambda ele: (-ele[1], -ele[2]), heap)
            
    def calc_dist(self, point):
        return point[0] ** 2 + point[1] ** 2