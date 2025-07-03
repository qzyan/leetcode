MAGIC_NUM = 31
HASH_SIZE = 10 ** 6

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            reuturn -1
        
        if len(needle) > len(haystack):
            return -1
        
        n_hash = self.hash(needle, len(needle))
        h_hash = self.hash(haystack, len(needle))
        base = self.calc_base(len(needle))

        for start_idx in range(0, len(haystack) - len(needle) + 1):
            if n_hash == h_hash and self.compare(haystack, needle, start_idx):
                return start_idx
            
            if start_idx == len(haystack) - len(needle):
                return -1
            
            h_hash = (h_hash * MAGIC_NUM + ord(haystack[start_idx + len(needle)])) % HASH_SIZE
            h_hash -= (ord(haystack[start_idx]) * base) % HASH_SIZE
            if h_hash < 0:
                h_hash += HASH_SIZE

        return -1

    def calc_base(self, size):
        base = 1
        for _ in range(size):
            base = (base * MAGIC_NUM) % HASH_SIZE
        
        return base

    def hash(self, s, size):
        result = 0
        for i in range(size):
            result = (result * MAGIC_NUM + ord(s[i])) % HASH_SIZE
        
        return result

    def compare(self, haystack, needle, start_idx):
        return haystack[start_idx:start_idx + len(needle)] == needle
