class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        
        min_len = float("inf")
        for string in strs:
            min_len = min(min_len, len(string))
            
        if min_len == 0:
            return ""
    
        left = 0
        right = min_len - 1
        
        while left < right:
            mid = (left + right) // 2
            if self.is_lcp(strs, mid):
                left = mid + 1
            else:
                right = mid - 1

        if self.is_lcp(strs, left):
            return strs[0][:left + 1]
        
        if self.is_lcp(strs, left - 1):
            return strs[0][:left]
        
        return ""
    
    def is_lcp(self, strs, index):
        for string in strs:
            if not string.startswith(strs[0][:index + 1]):
                return False
        
        return True
                
    
    