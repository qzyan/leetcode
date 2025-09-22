class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a

        # a     "11"
        # b "111111" 
        carry = 0
        result = []
        for i in range(len(b)):
            a_idx = len(a) - 1 - i
            b_idx = len(b) - 1 - i

            a_num = int(a[a_idx]) if a_idx >= 0 else 0
            b_num = int(b[b_idx])

            num = (a_num + b_num + carry) % 2
            carry = (a_num + b_num + carry) // 2

            result.append(num)

        if carry:
            result.append(1)

        result.reverse()
        return "".join([str(num) for num in result])