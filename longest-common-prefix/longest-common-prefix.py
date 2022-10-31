class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_arr = []
        is_char_in_common_prefix = True
        
        while is_char_in_common_prefix:
            first_str = strs[0]
            for char_idx, curr_char in enumerate(first_str):
                for str_idx in range(1, len(strs)):
                    curr_str = strs[str_idx]
                    if char_idx >= len(curr_str):
                        is_char_in_common_prefix = False
                        break
                    
                    if curr_str[char_idx] != curr_char:
                        is_char_in_common_prefix = False
                        break
                
                if is_char_in_common_prefix:
                    result_arr.append(curr_char)
                else:
                    break
                
            break
                
        return "".join(result_arr)