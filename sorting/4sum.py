class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        nums = sorted(nums)
        return self.k_sum(nums, 4, 0, target)

    def k_sum(self, nums, k, start_idx, target):
        if k == 2:
            return self.two_sum(nums, start_idx, target)
        results = []
        for idx in range(start_idx, len(nums) - k + 1):
            num = nums[idx]
            if num * k > target:
                break

            if idx > start_idx and nums[idx] == nums[idx - 1]:
                continue
            
            sub_results = self.k_sum(nums, k - 1, idx + 1, target - num)
            for sub_res in sub_results:
                results.append([num] + sub_res)

        return results

    def two_sum(self, nums, start_idx, target):
        left, right = start_idx, len(nums) - 1
        results = []
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                results.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
        
        return results

            

