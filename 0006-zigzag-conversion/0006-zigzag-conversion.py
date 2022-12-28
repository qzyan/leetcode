class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        
        if numRows == 1:
            return s
        
        arr = [[] for _ in range(numRows)]
        loop_size = numRows * 2 - 2
        for idx, char in enumerate(s):
            if idx % (loop_size) < numRows:
                arr_idx = idx % (loop_size)
                arr[arr_idx].append(char)
            else:
                arr_idx = numRows * 2 - 2 - idx % (loop_size)
                arr[arr_idx].append(char)
                for i in range(numRows):
                    if i == arr_idx:
                        continue
                    arr[i].append(' ')
        
        result_arr = []
        for chars in arr:
            for char in chars:
                if char == ' ':
                    continue
                result_arr.append(char)
        
        return "".join(result_arr)