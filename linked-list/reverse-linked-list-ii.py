# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        l_prev = self.find_node(dummy_head, left - 1)
        l_node = l_prev.next
        r_prev = self.find_node(dummy_head, right - 1)
        r_node = r_prev.next
        r_next = r_node.next
        r_node.next = None

        prev_node = None
        curr_node = l_prev.next
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        l_prev.next = r_node
        l_node.next = r_next

        return dummy_head.next

    def find_node(self, dummy_head, k):
        node = dummy_head
        for _ in range(k):
            node = node.next

        return node

        