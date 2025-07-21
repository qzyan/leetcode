class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        task_count_max_heap = []
        for task, count in task_count.items():
            heapq.heappush(task_count_max_heap, (-count, task))

        seq = []
        while task_count_max_heap:
            wait_list = []
            for _ in range(n + 1):
                if not task_count_max_heap:
                    if wait_list:
                        seq.append("idle")
                    else:
                        break
                else:
                    count, task = heapq.heappop(task_count_max_heap)
                    count = -count
                    seq.append(task)
                    count -= 1
                    if count:
                        wait_list.append((-count, task))

            for task in wait_list:
                heapq.heappush(task_count_max_heap, task)

        return len(seq)

            

