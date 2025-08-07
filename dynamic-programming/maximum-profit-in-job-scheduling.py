class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        profits = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        profits = sorted(profits)
        return self.dfs(0, profits, {})

    def dfs(self, curr_idx, profits, memo):
        if curr_idx == len(profits):
            return 0

        if curr_idx in memo:
            return memo[curr_idx]

        curr_start, curr_end, curr_profit = profits[curr_idx]
        # take this job
        next_workable_idx = self.find_first_start_after(profits, curr_end)
        profit1 = curr_profit + self.dfs(next_workable_idx, profits, memo)
        # skip this job
        profit2 = self.dfs(curr_idx + 1, profits, memo)

        memo[curr_idx] = max(profit1, profit2)
        return max(profit1, profit2)

    def find_first_start_after(self, profits, curr_end):
        left = 0
        right = len(profits) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if profits[mid][0] >= curr_end:
                right = mid
            else:
                left = mid

        if profits[left][0] >= curr_end:
            return left
        
        if profits[right][0] >= curr_end:
            return right
        
        return len(profits)

        