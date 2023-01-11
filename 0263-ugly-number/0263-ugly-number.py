class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        for factor in (2,3,5):
            while n % factor == 0:
                n = n // factor
            
        if n == 1:
            return True
        else:
            return False