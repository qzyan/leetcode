class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points = sorted(points)
        curr_end = float("inf")
        arrorw_count = 1

        for point in points:
            start, end = point
            if start > curr_end:
                arrorw_count += 1
                curr_end = end
            else:
                curr_end = min(curr_end, end)

        return arrorw_count
