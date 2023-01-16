class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        # not no interval << newInterval, -1
        left_idx = self.find_left_bound(intervals, newInterval)
        # if no interval >> newInterval, len(intervals)
        right_idx = self.find_right_bound(intervals, newInterval)
        
        if left_idx + 1 == right_idx:
            return intervals[:left_idx + 1] + [newInterval] + intervals[right_idx:]
        
        return self.combine_overlap(intervals, newInterval, left_idx, right_idx)
        
    def find_left_bound(self, intervals, newInterval):
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            idx += 1
            
        return idx - 1
    
    def find_right_bound(self, intervals, newInterval):
        idx = len(intervals) - 1
        while idx >= 0 and intervals[idx][0] > newInterval[1]:
            idx -= 1
            
        return idx + 1
    
    def combine_overlap(self, intervals, newInterval, left_idx, right_idx):
        combined_interval_start = min(intervals[left_idx + 1][0], newInterval[0])
        combined_interval_end = max(intervals[right_idx - 1][1], newInterval[1])
        combined_interval = [combined_interval_start, combined_interval_end]
        
        return intervals[:left_idx + 1] + [combined_interval] + intervals[right_idx:]