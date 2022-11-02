class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        
        start = count = 0
        while count < size:
            curr, prev = start, nums[start]
            while True:
                next_idx = (curr + k) % size
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1
                
                if curr == start:
                    break
                
            start += 1
            
        
            