class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(2)]
        dp[0][0] = True
        for row in range(len(s1) + 1):
            for col in range(len(s2) + 1):
                prev_state1 = dp[(row - 1) % 2][col] if row - 1 >= 0 else False
                prev_state2 = dp[row % 2][col - 1] if col - 1 >= 0 else False
                if not prev_state1 and not prev_state2:
                    continue
                
                if prev_state1 and s1[row - 1] == s3[row + col - 1]:
                    dp[row % 2][col] = True
                
                if prev_state2 and s2[col - 1] == s3[row + col - 1]:
                    dp[row % 2][col] = True

        return dp[len(s1) % 2][len(s2)]

