class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count_map = {}
        for task in tasks:
            count_map[task] = count_map.get(task, 0) + 1
        
        round_count = 0
        for task, count in count_map.items():
            if count % 3 == 0:
                round_count += count // 3
            elif count % 3 == 2:
                round_count += count // 3 + 1
            elif count == 1:
                return -1
            elif count % 3 == 1:
                round_count += count // 3 + 1
        
        return round_count