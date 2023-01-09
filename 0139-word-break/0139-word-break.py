class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        memo = [None] * len(s)
        return self.dfs(s, word_dict_set, 0, memo)
    
    
    def dfs(self, s, word_dict, start_idx, memo):
        if start_idx == len(s):
            return True
        
        if memo[start_idx] == False:
            return False
        
        for idx in range(start_idx + 1, len(s) + 1):
            word = s[start_idx: idx]
            if word not in word_dict:
                continue
            
            if self.dfs(s, word_dict, idx, memo):
                return True
        
        memo[start_idx] = False
        return False