class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        #[0, 1, 4, 5, 6] -> 3

        left = 0
        right = citations[-1]
        while left + 1 < right:
            mid = (left + right) // 2
            if citations[len(citations) - mid] >= mid:
                left = mid
            else:
                right = mid

        if citations[len(citations) - right] >= right:
            return right

        return left