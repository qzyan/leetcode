# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr_node = head
        while n > 0:
            curr_node = curr_node.next
            n -= 1

        prev_node = dummy
        while curr_node:
            curr_node = curr_node.next
            prev_node = prev_node.next

        prev_node.next = prev_node.next.next

        return dummy.next
