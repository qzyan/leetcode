# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        curr_node = head.next
        tail = head

        while curr_node:
            tail.next = curr_node.next
            curr_node.next = dummy.next
            dummy.next = curr_node

            curr_node = tail.next

        return dummy.next