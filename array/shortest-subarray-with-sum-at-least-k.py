class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        # prefix_sums[j] - prefix_sum[i] = sum of nums[i:j]
        min_len = float("inf")

        queue = collections.deque()
        for idx in range(len(prefix_sums)):
            while queue and prefix_sums[idx] <= prefix_sums[queue[-1]]:
                queue.pop()

            while queue and prefix_sums[idx] - prefix_sums[queue[0]] >= k:
                min_len = min(min_len, idx - queue.popleft())

            queue.append(idx)

        return min_len if min_len != float("inf") else -1
            
