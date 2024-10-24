class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        
        size = len(s)
        is_palindrome = [[False] * size for _ in range(size)]
        
        for i in range(size):
            is_palindrome[i][i] = True
            
        for i in range(1, size):
            is_palindrome[i][i - 1] = True
                
        longest_start = 0
        max_len = 1
        for length in range(2, size + 1):
            for start in range(size - length + 1):
                end = start + length - 1
                is_palindrome[start][end] = is_palindrome[start + 1][end - 1] and s[start] == s[end]
                
                if is_palindrome[start][end] and length > max_len:
                    longest_start = start
                    max_len = length
                    
        return s[longest_start:longest_start + max_len]
                    