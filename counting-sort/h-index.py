class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        #[0, 1, 4, 5, 6] -> 3

        left = 0
        right = citations[-1]
        if right == 0:
            return 0
        while left + 1 < right:
            mid = (left + right) // 2
            if len(citations) - mid < 0:
                right = mid
            elif citations[len(citations) - mid] >= mid:
                left = mid
            else:
                right = mid


        if len(citations) - right >= 0 and citations[len(citations) - right] >= right:
            return right

        return left