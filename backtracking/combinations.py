1;2;3
1,2;1,3;1,4;2,3;2,4;3,4

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        queue = deque([])

        for i in range(k):
            if not queue:
                for num in range(1, n + 2 - k):
                    queue.append([num])

                continue

            for idx in range(len(queue)):
                curr_comb = queue.popleft()
                last_digit = curr_comb[-1]
                for digit in range(last_digit + 1, n + 2 - k + i):
                    comb = curr_comb + [digit]
                    queue.append(comb)

        return list(queue)
