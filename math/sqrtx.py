class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 0
        right = x
        while left + 1 < right:
            mid = (left + right) // 2
            res = mid * mid
            if res == x:
                return mid
            if res < x:
                left = mid
            else:
                right = mid

        if right * right <= x:
            return right

        return left
