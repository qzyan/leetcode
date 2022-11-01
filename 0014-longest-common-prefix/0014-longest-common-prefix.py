class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_arr = []
        strs_len = len(strs)
        
        for index, char in enumerate(strs[0]):
            for str_idx in range(1, strs_len):
                string = strs[str_idx]
                if index >= len(string) or string[index] != char:
                    return "".join(result_arr)
                
            result_arr.append(char)
            
        return "".join(result_arr)