class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if num == dp[-1]:
                continue

            if len(dp) == 1:
                dp.append(num)
            elif num > dp[-1] and dp[-1] > dp[-2]:
                dp[-1] = num
            elif num > dp[-1] and dp[-1] < dp[-2]:
                dp.append(num)
                is_diff_pos = True
            elif num < dp[-1] and dp[-1] > dp[-2]:
                dp.append(num)
                is_diff_pos = False
            elif num < dp[-1] and not dp[-1] < dp[-2]:
                dp[-1] = num

        return len(dp)