class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while fast != slow:
            fast = self.get_next(fast)
            fast = self.get_next(fast)
            slow = self.get_next(slow)
        
        return fast == 1

    def get_next(self, num):
        res = 0
        while num:
            res += (num % 10) ** 2
            num = num // 10

        return res
