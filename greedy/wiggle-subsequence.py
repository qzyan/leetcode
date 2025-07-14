class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [nums[0]]
        is_diff_pos = False
        for i in range(1, len(nums)):
            num = nums[i]
            if num == dp[-1]:
                continue
            
            if num > dp[-1] and is_diff_pos:
                dp[-1] = num
            elif num > dp[-1] and not is_diff_pos:
                dp.append(num)
                is_diff_pos = True
            elif num < dp[-1] and is_diff_pos:
                dp.append(num)
                is_diff_pos = False
            else:
                dp[-1] = num

        return len(dp)