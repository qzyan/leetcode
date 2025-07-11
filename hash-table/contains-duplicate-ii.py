class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if k == 0:
            return False
        if nums[0] == nums[1]:
            return True

        slow = 0
        fast = 1
        uniques = set([nums[0]])
        while fast < len(nums):
            if fast - slow > k:
                uniques.remove(nums[slow])
                slow += 1
                continue
            
            if nums[fast] in uniques:
                return True
            
            uniques.add(nums[fast])
            fast += 1
        
        return False

