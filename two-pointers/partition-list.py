# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        tail = dummy2
        dummy1.next = head
        curr_node = head
        prev_node = dummy1

        while curr_node:
            if curr_node.val < x:
                curr_node = curr_node.next
                prev_node = prev_node.next
            else:
                prev_node.next = curr_node.next
                tail.next = curr_node
                tail = curr_node
                curr_node = curr_node.next

        prev_node.next = dummy2.next
        tail.next = None

        return dummy1.next
