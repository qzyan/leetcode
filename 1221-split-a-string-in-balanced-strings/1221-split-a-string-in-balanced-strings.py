class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return self.helper(s, 0)
    
    def helper(self, s, start_idx):
        if start_idx == len(s):
            return 0
        
        num_L = 0
        num_R = 0
        for idx in range(start_idx, len(s)):
            char = s[idx]
            if char == 'L':
                num_L += 1
            elif char == 'R':
                num_R += 1
                
            if num_L == num_R and num_L != 0:
                return 1 + self.helper(s, idx + 1)