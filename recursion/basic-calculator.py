class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        idx, result = self.calc_helper(s, 0)
        return result

    def calc_helper(self, s, idx):
        result = 0
        op = "+"
        while idx < len(s):
            char = s[idx]
            if char == " ":
                idx += 1
                continue

            if char == ")":
                idx += 1
                break

            if char == "(":
                idx, sub_res = self.calc_helper(s, idx + 1)
                result = self.calc(result, sub_res, op)
            elif char in "+-":
                op = char
                idx += 1
            else:
                num = 0
                while idx < len(s) and s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                    idx += 1

                result = self.calc(result, num, op)

        return idx, result

    def calc(self, result, num, op):
        if op ==  "+":
            return result + num
        else:
            return result - num

