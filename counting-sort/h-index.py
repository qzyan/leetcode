class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0] * 1001
        for citation in citations:
            counts[citation] += 1

        count = 0
        for idx in range(len(counts) - 1, -1, -1):
            count += counts[idx]
            if count >= idx:
                return idx

        return 0