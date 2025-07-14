class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        fp_count = 0
        bp_count = 0
        for char in s:
            if char not in ("(", ")"):
                res.append(char)
            if char == "(":
                res.append("(")
                fp_count += 1
            if char == ")" and fp_count > bp_count:
                res.append(")")
                bp_count += 1

        for i in range(len(res) - 1, -1, -1):
            char = res[i]
            if char == "(" and fp_count > bp_count:
                fp_count -= 1
                res[i] = ""

        return "".join(res)
            


        