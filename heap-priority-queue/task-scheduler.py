class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_count = max(task_count.values())

        idle_count = (max_count - 1) * (n + 1)
        for task, count in task_count.items():
            idle_count -= min(count, max_count - 1)
            if idle_count <= 0:
                break

        if idle_count <= 0:
            return sum(task_count.values())
        
        return sum(task_count.values()) + idle_count

            

