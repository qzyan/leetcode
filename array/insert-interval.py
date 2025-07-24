class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        results = []
        while idx < len(intervals):
            interval = intervals[idx]
            if interval[0] > newInterval[0]:
                break
            
            results.append(interval)
            idx += 1

        self.merge(results, newInterval)

        while idx < len(intervals):
            interval = intervals[idx]
            self.merge(results, interval)
            idx += 1

        return results

    def merge(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return
        
        last_interval = intervals[-1]
        if last_interval[-1] < interval[0]:
            intervals.append(interval)
        else:
            last_interval[-1] = max(last_interval[-1], interval[-1])
