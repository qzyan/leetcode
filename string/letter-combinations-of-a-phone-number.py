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

        results = []
        for digit in digits:
            if not results:
                for char in digit_chars[digit]:
                    results.append(char)
            else:
                new_results = []
                for result in results:
                    for char in digit_chars[digit]:
                        new_results.append(result + char)

                results = new_results

        return results