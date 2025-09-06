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
        while head:
            heapq.heappush(heap, (head.val, head))
            head = head.next

        dummy = ListNode()
        tail = dummy
        while heap:
            val, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

        tail.next = None

        return dummy.next
