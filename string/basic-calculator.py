class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        op = "+"
        idx = 0
        results = []
        ops = []
        while idx < len(s):
            char = s[idx]
            if char == " ":
                idx += 1
                continue
            
            if char == "(":
                results.append(result)
                ops.append(op)
                result = 0
                op = "+"
                idx += 1
            elif char == ")":
                num1 = results.pop()
                op = ops.pop()
                result = (num1 + result) if op == "+" else (num1 - result)
                idx += 1
            elif char in "+-":
                op = char
                idx += 1
            else:
                num = 0
                while idx < len(s) and s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                    idx += 1
                
                result = (result + num) if op == "+" else (result - num)

        return result