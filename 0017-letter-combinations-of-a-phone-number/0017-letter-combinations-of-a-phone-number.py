class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char_dict = {
            2: ("a", "b", "c"),
            3: ("d", "e", "f"),
            4: ("g", "h", "i"),
            5: ("j", "k", "l"),
            6: ("m", "n", "o"),
            7: ("p", "q", "r", "s"),
            8: ("t", "u", "v"),
            9: ("w", "x", "y", 'z')
        }
        if not digits:
            return []
        
        comb = []
        combs = []
        self.backtrack(num_char_dict, comb, combs, 0, digits)
        return combs
    
    def backtrack(self, num_char_dict, comb, combs, idx, digits):
        if idx == len(digits):
            combs.append(''.join(comb))
            return
        
        digit = int(digits[idx])
        chars = num_char_dict[digit]
        for char in chars:
            comb.append(char)
            self.backtrack(num_char_dict, comb, combs, idx + 1, digits)
            comb.pop()
        
        
        