class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        max_len = 0
        longest_pal = ""

        for i in range(2 * len(s) - 1):
            if i % 2 == 0:
                left, right = i // 2, i // 2
            else:
                left, right  = i // 2, i // 2 + 1
                
            start_idx, length = self.find_longest_pal(s, left, right)
            
            if length > max_len:
                max_len = length
                longest_pal = s[start_idx: start_idx + length]
                
        return longest_pal
                
    def find_longest_pal(self, s, left, right):
        if s[left] != s[right]:
            return -1, -1
        
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
                
            left -= 1
            right += 1
            
        return left + 1, right - left - 1
            
                
            
                
                