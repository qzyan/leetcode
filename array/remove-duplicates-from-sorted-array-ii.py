class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if fast - 1 >= 0 and nums[fast] == nums[fast - 1]:
                fast += 1
                continue

            if fast + 1 < len(nums) and nums[fast] == nums[fast + 1]:
                nums[slow], nums[slow + 1] = nums[fast], nums[fast + 1]
                slow += 2
                fast += 2
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        return slow
            
