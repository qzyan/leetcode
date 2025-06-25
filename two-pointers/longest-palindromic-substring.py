class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        if len(s) == 1:
            return s
        
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(1, len(s)):
            dp[i][i - 1] = True

        left, right = 0, 0
        for row in range(len(s) - 2, -1, -1):
            for col in range(row + 1, len(s)):
                if dp[row + 1][col - 1] == True and s[row] == s[col]:
                    dp[row][col] = True
                    if col - row > right - left:
                        right = col
                        left = row

        return s[left:right + 1]

