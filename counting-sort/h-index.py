class Solution:
    def hIndex(self, citations: List[int]) -> int:
        right = min(len(citations), max(citations))
        left = 0
        while left + 1 < right:
            mid = (left + right) // 2
            if self.exist_k_papers_cited_ge_k(citations, mid):
                left = mid
            else:
                right = mid

        if self.exist_k_papers_cited_ge_k(citations, right):
            return right

        return left

    def exist_k_papers_cited_ge_k(self, citations, k):
        count = 0
        for c in citations:
            if c >= k:
                count += 1
        
        return count >= k