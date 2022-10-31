class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_size = len(haystack)
        needle_size = len(needle)
        
        for i in range(haystack_size - needle_size + 1):
            if haystack[i:i + needle_size] == needle:
                return i
            
        return -1
