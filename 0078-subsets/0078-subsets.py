class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combs = [[]]
        for num in nums:
            new_combs = []
            for comb in combs:
                new_comb = comb[:] + [num]
                new_combs.append(new_comb)
            combs.extend(new_combs)
                
        return combs