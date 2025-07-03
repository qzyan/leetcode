class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []

        nums = sorted(nums)
        return self.k_sum(nums, 0, 4, target)

    def k_sum(self, nums, start_idx, k, target):
        if k == 2:
            return self.two_sum(nums, start_idx, target)

        results = []
        for idx in range(start_idx, len(nums) - k + 1):
            if idx != start_idx and nums[idx] == nums[idx - 1]:
                continue
            
            if nums[idx] * k > target:
                break
            
            sub_results = self.k_sum(nums, idx + 1, k - 1, target - nums[idx])
            for sub_result in sub_results:
                result = ([nums[idx]] + sub_result) 
                results.append(result)

        return results

    def two_sum(self, nums, start_idx, target):
        left = start_idx
        right = len(nums) - 1
        results = []
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                results.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif total < target:
                left += 1
            else:
                right -= 1

        return results