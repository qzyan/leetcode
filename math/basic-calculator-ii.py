class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        for idx in range(len(s)):
            char = s[idx]
            if char == " ":
                idx += 1
                continue

            if char.isdigit():
                num = 0
                while idx < len(s) and s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                    idx += 1

                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    prev_num = stack.pop()
                    stack.append(num * prev_num)
                else:
                    prev_num = stack.pop()
                    stack.append(int(prev_num / num))
            else:
                op = char

        return sum(stack)