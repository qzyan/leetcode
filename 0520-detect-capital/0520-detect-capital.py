class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_upeprcase_idx = None
        upper_count = 0
        for idx, char in enumerate(word):
            if char.islower():
                continue
            
            if upper_count == 0:
                first_upeprcase_idx = idx
            upper_count += 1
        
        print(upper_count)
        
        if upper_count == 0:
            return True
        if upper_count == 1 and first_upeprcase_idx == 0:
            return True
        if upper_count == len(word):
            return True
        
        return False
                
                
                