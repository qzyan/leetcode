class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        print(task_count)
        max_heap = [(-c, task) for task, c in task_count.items()]
        heapq.heapify(max_heap)
        seq = []

        while max_heap:
            wait_list = []
            for _ in range(n + 1):
                if max_heap:
                    count, task = heapq.heappop(max_heap)
                    count = -count
                    seq.append(task)
                    count -= 1
                    if count:
                        wait_list.append((-count, task))
                else:
                    if wait_list:
                        seq.append("idle")

            while wait_list:
                heapq.heappush(max_heap, wait_list.pop())

        return len(seq)
