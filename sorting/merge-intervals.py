class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged_intervals = []
        for interval in intervals:
            self.merge_or_append(merged_intervals, interval)

        return merged_intervals

    def merge_or_append(self, merged_intervals, interval):
        if not merged_intervals:
            merged_intervals.append(interval)
            return

        last_interval = merged_intervals[-1]
        if last_interval[-1] < interval[0]:
            merged_intervals.append(interval)
        else:
            last_interval[-1] = max(last_interval[-1], interval[-1])
        