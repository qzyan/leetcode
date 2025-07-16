class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count_mapping = self.count_task(tasks)
        task_counts = []
        max_count = 0
        for task, count in task_count_mapping.items():
            task_counts.append((task, count))
            max_count = max(max_count, count)

        idle_count = (max_count - 1) * (n + 1)
        for task, count in task_counts:
            idle_count -= min(count, max_count - 1)

        return len(tasks) + max(0, idle_count)

    def count_task(self, tasks):
        mapping = {}
        for task in tasks:
            mapping[task] = mapping.get(task, 0) + 1

        return mapping