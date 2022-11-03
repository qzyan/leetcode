import collections

DIGITS = [i for i in range(10)]

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)
        root = "0000"
        if root in deadset:
            return -1
        queue = collections.deque()
        visited = set()
        
        visited.add(root)
        queue.append(root)
        step = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_code = queue.popleft()
                if curr_code == target:
                    return step

                next_codes = self.create_next_codes(curr_code, deadset)
                for next_code in next_codes:
                    if next_code in visited:
                        continue
                    visited.add(next_code)
                    queue.append(next_code)
            
            step += 1
            
        return -1
    
    def create_next_codes(self, code, deadends):
        results = []
        code_digits = [*code]
            
        for i in range(4):
            ith_cur_digit = code_digits[i]
            ith_new_digit_1 = str(DIGITS[(int(ith_cur_digit) + 1) % 10])
            ith_new_digit_2 = str(DIGITS[(int(ith_cur_digit) - 1) % 10])
            
            code_digits[i] = ith_new_digit_1
            new_code = "".join(code_digits)
            if new_code not in deadends:
                results.append(new_code)
            
            code_digits[i] = ith_new_digit_2
            new_code = "".join(code_digits)
            if new_code not in deadends:
                results.append(new_code)
            
            code_digits[i] = ith_cur_digit
        
        return results
