class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        results = deque([])
        for digit in digits:
            if not results:
                for char in digit_chars[digit]:
                    results.append(char)
            else:
                for _ in range(len(results)):
                    curr_comb = results.popleft()
                    for char in digit_chars[digit]:
                        results.append(curr_comb + char)

        return list(results)