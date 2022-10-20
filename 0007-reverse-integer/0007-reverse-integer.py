class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        result = 0
        isNeg = False
        
        if x < 0: 
            isNeg = True
        
        x = abs(x)

        
        while x > 0:
            remainder = x % 10
            
            # see if the result will be in range when * 10 + remainder
            if result > INT_MAX / 10:
                return 0
            if result == INT_MAX // 10 and remainder > 7:
                return 0
                
            result = result * 10 + (remainder)
            x = x // 10
        
        if isNeg:
            result = -result
        
        return result