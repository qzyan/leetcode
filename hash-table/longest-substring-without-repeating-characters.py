class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        unique_chars = set()
        slow, fast = 0, 0
        longest_len = 1
        
        while fast < len(s):
            while s[fast] in unique_chars:
                unique_chars.remove(s[slow])

                slow += 1

            unique_chars.add(s[fast])
            if fast - slow + 1 > longest_len:
                longest_len = fast - slow + 1
            
            fast += 1

        return longest_len
            