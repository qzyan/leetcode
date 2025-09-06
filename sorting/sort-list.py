# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        heap = []
        idx = 0
        while head:
            heapq.heappush(heap, (head.val, idx, head))
            head = head.next
            idx += 1

        dummy = ListNode()
        tail = dummy
        while heap:
            val, idx, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

        tail.next = None

        return dummy.next
