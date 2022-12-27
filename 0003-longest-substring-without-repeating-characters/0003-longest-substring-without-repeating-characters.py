class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left = 0
        right = 0
        max_size = 1
        unique = set()
        
        while right < len(s):
            curr_char = s[right]
            while curr_char in unique:
                left_char = s[left]
                unique.remove(left_char)
                left += 1
            
            max_size = max(max_size, right - left + 1)
            unique.add(curr_char)
            right += 1
        
        return max_size