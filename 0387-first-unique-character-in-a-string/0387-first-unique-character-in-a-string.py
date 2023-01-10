class Solution:
    def firstUniqChar(self, s: str) -> int:
        # {"a": [count, first_idx]}
        mapping = {}
        for idx, char in enumerate(s):
            if char in mapping:
                mapping[char][0] += 1
            else:
                mapping[char] = [1, idx]
        
        first_idx = float('inf')
        for key, val in mapping.items():
            count, idx = val
            if count == 1:
                first_idx = min(first_idx, idx)
        
        
        return first_idx if first_idx != float('inf') else -1