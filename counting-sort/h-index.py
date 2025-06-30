class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        #[0, 1, 4, 5, 6] -> 3

        left = 0
        right = len(citations)
        while left + 1 < right:
            mid = (left + right) // 2
            idx = len(citations) - mid
            if citations[idx] >= mid:
                left = mid
            else:
                right = mid

        idx = len(citations) - right
        if citations[idx] >= right:
            return right
        
        return left