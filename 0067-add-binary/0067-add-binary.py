class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        
        carry = 0
        reversed_result_arr = []
        for i in range(-1, - max(a_len, b_len) - 1, -1):
            a_num = int(a[i]) if i >= -a_len else 0
            b_num = int(b[i]) if i >= -b_len else 0
            
            num = (a_num + b_num + carry) % 2
            carry = (a_num + b_num + carry) // 2
            reversed_result_arr.append(str(num))
            
        if carry:
            reversed_result_arr.append('1')
            
        return ''.join(reversed(reversed_result_arr))