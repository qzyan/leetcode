class Solution:
    def reverseWords(self, s: str) -> str:
        words = self.remove_space(s)
        self.reverse(words, 0 , len(words) - 1)
        self.reverse_each_word(words)
        
        return "".join(words)
    
    def remove_space(self, s):
        result = []
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == " ":            
            left += 1
            
        while left < right and s[right] == " ":            
            right -= 1
            
        prev = None
        for curr in range(left, right + 1):
            if s[curr] == prev == " ":
                continue
            
            result.append(s[curr])
            prev = s[curr]
            
        return result
    
    def reverse(self, words, left, right):      
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
            
        return
    
    def reverse_each_word(self, words):
        start = 0
        while start < len(words):
            end = start
            while end < len(words) - 1 and words[end + 1] != " ":
                end += 1
            
            self.reverse(words, start, end)
            
            start = end + 2
        
        return