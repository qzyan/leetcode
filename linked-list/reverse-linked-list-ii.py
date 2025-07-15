# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        idx = 0
        node = dummy
        while idx < left - 1:
            node = node.next
            idx += 1

        l_prev_node = node

        idx += 1
        node = node.next
        l_node = node

        prev_node = None
        while idx <= right:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
            idx += 1

        l_prev_node.next = prev_node
        l_node.next = node

        return dummy.next
        




