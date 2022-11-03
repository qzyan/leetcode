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

                next_codes = self.create_next_codes(curr_code)
                for next_code in next_codes:
                    if next_code in visited or next_code in deadset:
                        continue
                    visited.add(next_code)
                    queue.append(next_code)
            
            step += 1
            
        return -1
    
    def create_next_codes(self, code):
        results = []
        for i in range(4):
            curr_digit = int(code[i])
            for add in (-1, 1):
                new_digit = (curr_digit + add) % 10
                new_code = code[:i] + str(new_digit) + code[i + 1:]
                results.append(new_code)
        
        return results
