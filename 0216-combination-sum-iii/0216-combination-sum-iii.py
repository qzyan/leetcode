class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        comb = []
        combs = []
                
        self.backtrack(comb, combs, nums, 0, k, n)
        return combs
    
    def backtrack(self, comb, combs, nums, start_idx, k, target):
        if target == 0 and k == 0:
            combs.append(comb[:])
        
        if k == 0:
            return
        
        for idx in range(start_idx, len(nums)):            
            num = nums[idx]
            if num > target:
                break
            
            comb.append(num)
            self.backtrack(comb, combs, nums, idx + 1, k - 1, target - num)
            comb.pop()
            