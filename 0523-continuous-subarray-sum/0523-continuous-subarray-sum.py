class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_first_i_mapping = {0: 0}
        curr_sum = 0
        for idx, num in enumerate(nums):
            curr_sum += num
            curr_remainder = curr_sum % k
            if curr_remainder in remainder_first_i_mapping:
                i = remainder_first_i_mapping[curr_remainder]
                if idx + 1 - i > 1:
                    return True
            else:
                remainder_first_i_mapping[curr_remainder] = idx + 1
        
        return False
            
            