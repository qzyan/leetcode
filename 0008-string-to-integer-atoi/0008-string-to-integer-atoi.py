class Solution:
    def myAtoi(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        
        MAX = 2**31 - 1
        MIN = -(2**31)
        result = 0
        isPositive = True
        n = len(s)
        index = 0        

        
        
        # ignore all the white space
        while index < n and s[index] == ' ':
            index += 1
        
        # special case:
        if index >= n:
            return 0
        
        # get the pos/neg symbol 
        if s[index] == '-':
            isPositive = False
            index += 1
        elif s[index] == '+':
            index += 1
        
        # get all the digit
        while index < n and s[index].isdecimal():
            # see if in range
            if isPositive and result <= (MAX - int(s[index])) / 10:
                result = result * 10 + int(s[index])
                index += 1
                continue
                
            if isPositive and result > (MAX - int(s[index])) / 10:
                result = MAX
                return result 
            
            if not isPositive and result >= (MIN + int(s[index])) / 10:
                result = result * 10 - int(s[index])
                index += 1
                continue
                
            if not isPositive and result < (MIN + int(s[index])) / 10:
                result = MIN
                return result
        
        return result 
                
        
        
            