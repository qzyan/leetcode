class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count_mapping = self.count_task(tasks)
        task_counts = []
        for task, count in task_count_mapping.items():
            task_counts.append((task, count))
        
        task_counts.sort(key=lambda x: (x[1], x[0]))
        max_count = task_counts[-1][1]

        idle_count = (max_count - 1) * (n + 1)
        for task, count in task_counts:
            idle_count -= min(count, max_count - 1)

        return len(tasks) + max(0, idle_count)

    def count_task(self, tasks):
        mapping = {}
        for task in tasks:
            mapping[task] = mapping.get(task, 0) + 1

        return mapping