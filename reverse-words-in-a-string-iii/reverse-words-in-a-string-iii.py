class Solution:
    def reverseWords(self, s: str) -> str:
        words = [*s]
        start = 0
        while start < len(words):
            end = start
            while end < len(words) and words[end] != " ":
                end += 1
                
            self.reverse(words, start, end - 1)
            start = end + 1
            
        return "".join(words)

    def reverse(self, words, left, right):
        while left < right:
            words[left], words[right] = words[right], words[left]
            
            left += 1
            right -= 1
        
        return
        