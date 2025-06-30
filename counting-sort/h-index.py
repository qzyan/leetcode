class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        left = 0
        right = citations[-1]
        while left + 1 < right:
            mid = (left + right ) // 2
            if self.count_of_paper_with_c_le(citations, mid) >= mid:
                left = mid
            else:
                right = mid

        
        if self.count_of_paper_with_c_le(citations, right) >= right:
            return right

        return left

    def count_of_paper_with_c_le(self, citations, target):
        left = 0
        right = len(citations) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if citations[mid] >= target:
                right = mid
            else:
                left = mid

        if citations[left] >= target:
            return len(citations) - left
        if citations[right] >= target:
            return len(citations) - right

        return 0


         