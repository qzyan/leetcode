class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([startGene])
        visited = set([startGene])
        bank = set(bank)

        step = 0
        while queue:
            for _ in range(len(queue)):
                curr_gene = queue.popleft()

                if curr_gene == endGene:
                    return step

                for next_gene in self.get_neighbors(curr_gene, bank):
                    if next_gene in visited:
                        continue
                    
                    queue.append(next_gene)

            step += 1

        return -1

    def get_neighbors(self, curr_gene, bank):
        neighbors = []
        for idx in range(len(curr_gene)):
            for char in "ACGT":
                if char == curr_gene[idx]:
                    continue

                new_gene = curr_gene[:idx] + char + curr_gene[idx + 1:]

                if new_gene in bank:
                    neighbors.append(new_gene)

        return neighbors
