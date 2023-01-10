class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_L = 0
        num_R = 0
        count = 0
        
        for idx in range(len(s)):
            char = s[idx]
            if char == 'L':
                num_L += 1
            elif char == 'R':
                num_R += 1
                
            if num_L == num_R and num_L != 0:
                num_L = 0
                num_R = 0
                count += 1
                
        return count