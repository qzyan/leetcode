# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        idx = 0
        dummy = ListNode()
        dummy.next = head

        node = dummy
        prev_node = None
        while idx < k:
            prev_node = node
            node = node.next
            idx += 1

        prev_node1 = prev_node
        slow_node = dummy

        while node.next:
            node = node.next
            slow_node = slow_node.next


        prev_node2 = slow_node
        
        node1 = prev_node1.next
        node2 = prev_node2.next

        node1.val, node2.val = node2.val, node1.val

        return dummy.next

