class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = 0
        end = len(strs) - 1
        
        return self.lcp_helper(strs, start, end)
    
    def lcp_helper(self, strs, start, end):
        if start == end:
            return strs[start]
        
        mid = (start + end) // 2
        lcp_left = self.lcp_helper(strs, start, mid)
        lcp_right = self.lcp_helper(strs, mid + 1, end)
        return self.lcp_between_two(lcp_left, lcp_right)
    
    def lcp_between_two(self, str1, str2):
        min_len = min(len(str1), len(str2))
        
        for idx in range(min_len):
            if str1[idx] != str2[idx]:
                return str1[:idx]
            
        return str1[:min_len]
                