# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if not node:
                continue

            heapq.heappush(heap, (node.val, idx, node))

        dummy = ListNode()
        tail = dummy
        while heap:
            curr_val, idx, curr_node = heapq.heappop(heap)
            tail.next = curr_node
            tail = tail.next

            curr_node = curr_node.next
            if curr_node:
                heapq.heappush(heap, (curr_node.val, idx, curr_node))

        return dummy.next