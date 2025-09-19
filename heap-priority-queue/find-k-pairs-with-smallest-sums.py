class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        visited = set()
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        result = []


        while heap and k:
            curr_sum, p1, p2 = heapq.heappop(heap)
            result.append((nums1[p1], nums2[p2]))
            
            if p1 + 1 < len(nums1) and (p1 + 1, p2) not in visited:
                heapq.heappush(heap, (nums1[p1 + 1] + nums2[p2], p1 + 1, p2))
                visited.add((p1 + 1, p2))
            
            if p2 + 1 < len(nums2) and (p1, p2 + 1) not in visited:
                heapq.heappush(heap, (nums1[p1] + nums2[p2 + 1], p1, p2 + 1))
                visited.add((p1, p2 + 1))
            
            k -= 1

        return result
