class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        fp_count = 0
        bp_count = 0
        for char in s:
            if char not in ("(", ")"):
                stack.append(char)
            
            if char == "(":
                stack.append("(")
                fp_count += 1
            
            if char == ")" and fp_count > bp_count:
                stack.append(")")
                bp_count += 1


        result = []
        for i in range(len(stack) - 1, -1, -1):
            char = stack[i]
            if char == "(" and fp_count > bp_count:
                fp_count -= 1
                continue
            
            result.append(char)

        result.reverse()
        return "".join(result)
            


        