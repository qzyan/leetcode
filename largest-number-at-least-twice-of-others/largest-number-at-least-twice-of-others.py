class Solution:
    def dominantIndex(self, nums: List[int]) -> int:       
        largest_index = None
        largest = -float("inf")
        second_largest = -float("inf")
        
        for index, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                largest_index = index
            
            if largest > num > second_largest:
                second_largest = num
                
        if largest >= 2 * second_largest:
            return largest_index
        
        return -1