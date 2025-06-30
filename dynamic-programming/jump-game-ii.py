class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = collections.deque([0])
        furthest_idx = 0
        step = 0

        while queue:
            end_idx = furthest_idx
            for _ in range(len(queue)):
                curr_idx = queue.popleft()
                if curr_idx == len(nums) - 1:
                    return step

                furthest_idx = max(furthest_idx, curr_idx + nums[curr_idx])

            step += 1

            for idx in range(end_idx + 1, min(furthest_idx + 1, len(nums))):
                queue.append(idx)

        return step

