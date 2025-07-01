class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""

        chars = [char for char in s]
        self.clean_space(chars)
        self.reverse(chars, 0, len(chars) - 1)
        self.reverse_word(chars)

        return "".join(chars)

    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    
    def reverse_word(self, chars):
        slow, fast = 0, 0
        while fast < len(chars):
            if fast + 1 == len(chars) or chars[fast + 1] == " ":
                self.reverse(chars, slow, fast)
                slow, fast = fast + 2, fast + 2
            else:
                fast += 1
        
    def clean_space(self, chars):
        slow = 0
        fast = 0
        end = len(chars) - 1
        while fast < len(chars) and chars[fast] == " ":
                fast += 1

        while end >= 0 and chars[end] == " ":
                end -= 1
        
        while fast <= end:
            if fast - 1 >= 0 and chars[fast] == " " and chars[fast - 1] == " ":
                fast += 1
            else:
                chars[slow] = chars[fast]
                fast += 1
                slow += 1

        chars[:] = chars[:slow] 
        

        