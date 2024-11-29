class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dec_stack = collections.deque()
        ans = []
        for i in range(len(nums)):
            if i < k - 1:
                while dec_stack and nums[i] >= dec_stack[-1][0]:
                    dec_stack.pop()
                dec_stack.append((nums[i], i))
                continue
            
            left_idx = i - k + 1
            
            if dec_stack and dec_stack[0][1] < left_idx:
                dec_stack.popleft()
            
            while dec_stack and dec_stack[-1][0] <= nums[i]:
                dec_stack.pop()
            dec_stack.append((nums[i], i))
            
            ans.append(dec_stack[0][0])

        
        return ans

            
            