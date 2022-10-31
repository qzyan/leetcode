class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        
        new_digit = (digits[-1] + 1) % 10
        carry = (digits[-1] + 1) // 10
        result.append(new_digit)
        
        for i in range(len(digits) - 2, -1, -1):
            new_digit = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            result.append(new_digit)
        
        if carry == 1:
            result.append(1)
        
        return reversed(result)
        
            