class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.calc(num1, num2, token)
                stack.append(result)

        return sum(stack)

    def calc(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2

        if op == "*":
            return num1 * num2

        if op == "/":
            return int(num1 / num2)