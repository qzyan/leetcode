class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sums = [0] * (len(nums) + 1)
        sum_val = 0
        for idx, num in enumerate(nums):
            sum_val += num
            prefix_sums[idx + 1] = sum_val

        queue = deque() # mono queue, [1,3,5, 10] prefix[idx] inc
        length = float("inf")
        for idx in range(len(prefix_sums)):
            prefix_sum = prefix_sums[idx]
            while queue and prefix_sums[queue[-1]] >= prefix_sum:
                queue.pop()

            queue.append(idx)
            while queue and prefix_sum - prefix_sums[queue[0]] >= k:
                length = min(length, idx - queue.popleft())

        return length if length != float("inf") else -1
        
