class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().rstrip()
        words = s.split()
        words.reverse()
        result = ' '.join(words)
        return result