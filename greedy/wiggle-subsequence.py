class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [nums[0]]
        is_up = 0

        for i in range(1, len(nums)):
            num = nums[i]
            if num == dp[-1]:
                continue
            
            if is_up == 0:
                is_up = num - dp[-1]
                dp.append(num)
            elif is_up > 0:
                if num > dp[-1]:
                    dp[-1] = num
                elif num < dp[-1]:
                    is_up = num - dp[-1]
                    dp.append(num)
            elif is_up < 0:
                if num > dp[-1]:
                    is_up = num - dp[-1]
                    dp.append(num)
                elif num < dp[-1]:
                    dp[-1] = num

        return len(dp)


        