class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        isNeg = False
        
        if x < 0: 
            isNeg = True
        
        x = abs(x)

        
        while x > 0:
            remainder = x % 10
            result = result * 10 + (remainder)
            x = x // 10
        
        if isNeg:
            result = -result
        
        if result > 2**31 - 1 or result < -(2**31):
            return 0
        
        return result