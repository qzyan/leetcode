class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # build the num_char mapping
        num_char_mapping = self.build_mapping()
        results = [[]]
        for num in digits:
            new_results = []
            for result in results:
                for char in num_char_mapping[num]:  
                    new_result = result[:]
                    new_result.append(char)
                    new_results.append(new_result)
            results = new_results
            
        return map(lambda arr : "".join(arr), results)
    
    def build_mapping(self):
        return {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        # iterate over each num in the digits string
            # iternate over each letter in the mapping
                # iterate over each result in results
                    # append the letter to the result
                    # append the result to new_results
            # result = new_results
                    
        # map the results to string results
        # return the results
        