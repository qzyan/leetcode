class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_max_heap = self.count_tasks(tasks) # [(-3, A), (-2, B)]
        heapq.heapify(task_max_heap)
        seq = []
        idx = 0
        while task_max_heap:
            waiting_tasks = []
            for i in range(n + 1):
                if not task_max_heap and waiting_tasks:
                    seq.append("idle")
                    continue
                
                if task_max_heap:
                    task_count, task = heapq.heappop(task_max_heap)
                    task_count = -task_count
                    task_count -= 1
                    seq.append(task)

                    if task_count > 0:
                        waiting_tasks.append((-task_count, task))

            for task in waiting_tasks:
                heapq.heappush(task_max_heap, task)

        return len(seq)

                 
            
            

        return len(seq)

    def count_tasks(self, tasks):
        mapping = {}
        for task in tasks:
            mapping[task] = mapping.get(task, 0) + 1

        results = []
        for task, count in mapping.items():
            results.append((-count, task))

        return results

