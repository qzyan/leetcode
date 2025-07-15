# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr_node = head
        prev_tail = dummy
        while curr_node:
            last_node, next_head = self.split(curr_node, k)
            if last_node is None:
                break
            
            self.reverse(curr_node, last_node)
            prev_tail.next = last_node
            curr_node.next = next_head
            prev_tail = curr_node
            curr_node = next_head

        return dummy.next

    def split(self, node, k):
        while node and k > 1:
            node = node.next
            k -= 1

        if node is None:
            return None, None
        
        next_head = node.next
        node.next = None
        return node, next_head

    def reverse(self, left_node, right_node):
        prev_node = None
        node = left_node
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        



