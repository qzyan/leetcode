class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        copied_points = points[:]
        return self.quick_select(copied_points, 0, len(copied_points) - 1, k)
        
    
    # get the k smallest 
    def quick_select(self, points, start, end, k):
        if start >= end:
            return points[:k]
        
        left = start
        right = end
        mid = (left + right) // 2
        pivot = points[mid]
        
        while left <= right:
            while left <= right and self.calc_dist(points[left]) < self.calc_dist(pivot):
                left += 1
            while left <= right and self.calc_dist(points[right]) > self.calc_dist(pivot):
                right -= 1
            
            if left <= right:
                points[left], points[right] = points[right], points[left]
                left += 1
                right -= 1
                
        if k - 1 >= left:
            return self.quick_select(points, left, end, k)
        if k - 1 <= right:
            return self.quick_select(points, start, right, k)
        return points[:k]
    
    def calc_dist(self, point):
        return point[0] ** 2 + point[1] ** 2