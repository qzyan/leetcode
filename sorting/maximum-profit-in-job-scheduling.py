class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        profits = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        # sort by endtime
        profits = sorted(profits, key=lambda x: (x[1], x[0], x[2]))
        dp = [0] * n

        for idx in range(n):
            dp[idx] = max(dp[idx], dp[idx - 1]) if idx - 1 >= 0 else 0 # skip this job
            last_end_before_idx = self.find_last_end_before_job(profits, profits[idx][0])

             # take this job and add prev
            if last_end_before_idx == -1:
                dp[idx] = max(dp[idx], profits[idx][2])
            else:
                dp[idx] = max(dp[idx], dp[last_end_before_idx] + profits[idx][2])

        return dp[-1]

    def find_last_end_before_job(self, profits, start_time):
        left = 0
        right = len(profits) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if profits[mid][1] <= start_time:
                left = mid
            else:
                right = mid

        if profits[right][1] <= start_time:
            return right
        
        if profits[left][1] <= start_time:
            return left
        
        return -1
