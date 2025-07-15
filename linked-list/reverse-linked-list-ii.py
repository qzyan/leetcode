# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l_prev_node = self.find_node(dummy, left - 1)
        r_prev_node = self.find_node(dummy, right - 1)
        l_node = l_prev_node.next
        r_node = r_prev_node.next
        r_next_node = r_node.next
        r_node.next = None

        prev_node = None
        curr_node = l_node
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        l_prev_node.next = r_node
        l_node.next = r_next_node

        return dummy.next

    def find_node(self, head, k):
        while k > 0:
            head = head.next
            k -= 1

        return head



