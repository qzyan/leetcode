class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        code_string_mapping = {}
        for string in strs:
            code = self.encode(string)
            if code not in code_string_mapping:
                code_string_mapping[code] = [string]
            else:
                code_string_mapping[code].append(string)

        results = []
        for val in code_string_mapping.values():
            results.append(val)

        return results
    
    def encode(self, string):
        code = [0] * 26
        for char in string:
            code[ord(char) - ord("a")] += 1

        return tuple(code)
