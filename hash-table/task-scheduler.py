class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_max_heap = self.count_tasks(tasks) # [(-3, A), (-2, B)]
        heapq.heapify(task_max_heap)
        idle_tasks = []

        seq = []
        idx = 0
        while task_max_heap or idle_tasks:
            while idx < n + 1:
                if not task_max_heap and not idle_tasks:
                    break

                if not task_max_heap:
                    seq.append("idle")
                    idx += 1
                    continue

                task_count, task = heapq.heappop(task_max_heap)
                task_count = -task_count
                seq.append(task)

                task_count -= 1
                if task_count != 0:
                    idle_tasks.append((-task_count, task))
                
                idx += 1
            
            idx = 0
            for idle_task in idle_tasks:
                heapq.heappush(task_max_heap, idle_task)
            
            idle_tasks = []
            

        return len(seq)

    def count_tasks(self, tasks):
        mapping = {}
        for task in tasks:
            mapping[task] = mapping.get(task, 0) + 1

        results = []
        for task, count in mapping.items():
            results.append((-count, task))

        return results

