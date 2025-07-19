class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""

        unmatched_opens = []
        unmatched_closes = []
        for idx in range(len(s)):
            a = s[idx]
            if a == "(":
                unmatched_opens.append(idx)
            elif a == ")":
                if unmatched_opens:
                    unmatched_opens.pop()
                else:
                    unmatched_closes.append(idx)
        
        results = [c for c in s]
        for idx in unmatched_opens:
            results[idx] = ""
        
        for idx in unmatched_closes:
            results[idx] = ""

        return "".join(results)
            