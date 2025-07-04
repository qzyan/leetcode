class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp1 = [{} for _ in range(k + 1)]
        dp2 = [[0] * len(nums) for _ in range(k + 1)]

        for col in range(len(nums)):
            num = nums[col]
            dp1[0][num] = dp1[0].get(num, 0) + 1
            dp2[0][col] = max(dp2[0][col - 1], dp1[0][num]) if col - 1 >= 0 else dp1[0][num]

        for row in range(1, k + 1):
            for col in range(1, len(nums)):
                num = nums[col]
                dp1[row][num] = max(dp1[row].get(num, 0) + 1, dp2[row - 1][col - 1] + 1)
                dp2[row][col] = max(dp2[row][col - 1], dp1[row][num]) if col - 1 >= 0 else dp1[row][num]

        return max([dp2[row][-1] for row in range(k + 1)])
