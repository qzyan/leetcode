class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]

        for idx, char in enumerate(s):
            j = idx % (numRows * 2 - 2)
            if j < numRows:
                row_idx = j
            else:
                row_idx = numRows * 2 - 2 - j
            
            rows[row_idx].append(char)

        strings = ["".join(row) for row in rows]
        return "".join(strings)