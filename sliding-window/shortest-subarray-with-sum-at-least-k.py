class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        for num in nums:
            curr_sum = num + prefix_sums[-1]
            prefix_sums.append(curr_sum)

        queue = collections.deque()
        min_len = float("inf")
        for idx in range(len(prefix_sums)):
            curr_prefix_sum = prefix_sums[idx]
            while queue and prefix_sums[queue[-1]] >= curr_prefix_sum:
                queue.pop()

            queue.append(idx)
            while queue and curr_prefix_sum - prefix_sums[queue[0]] >= k:
                min_len = min(min_len, idx - queue.popleft())

        return min_len if min_len != float("inf") else -1