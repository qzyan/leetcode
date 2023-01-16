class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left_idx = self.find_left_interval(intervals, newInterval)
        right_idx = self.find_right_interval(intervals, newInterval)
        
        if left_idx + 1 == right_idx:
            intervals.insert(right_idx, newInterval)
            return intervals
        
        return self.combine(intervals, left_idx, right_idx, newInterval)
        
    def find_left_interval(self, intervals, newInterval):
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            idx += 1
            
        return idx - 1
    
    def find_right_interval(self, intervals, newInterval):
        idx = len(intervals) - 1
        while idx >= 0 and intervals[idx][0] > newInterval[1]:
            idx -= 1
        
        return idx + 1
    
    def combine(self, intervals, left_idx, right_idx, newInterval):
        new_start = min(intervals[left_idx + 1][0], newInterval[0])
        new_end = max(intervals[right_idx - 1][1], newInterval[1])
        return intervals[:left_idx + 1] + [[new_start, new_end]] + intervals[right_idx:]
        