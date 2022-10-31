class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        
        carry = 0
        reversed_result_arr = []
        for i in range(-1, - max(a_len, b_len) - 1, -1):
            a_num = a[i] if i >= -a_len else '0'
            b_num = b[i] if i >= -b_len else '0'
            
            if a_num == '1':
                carry += 1
            if b_num == '1':
                carry += 1
            
            if carry % 2 == 1:
                reversed_result_arr.append('1')
            else: 
                reversed_result_arr.append('0')
            
            carry = carry // 2
            
        if carry:
            reversed_result_arr.append('1')
            
        return ''.join(reversed(reversed_result_arr))