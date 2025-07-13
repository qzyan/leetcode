# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head

        prev_tail = dummy
        while prev_tail:
            last_node, next_head = self.split(prev_tail, k)
            if not last_node:
                break
            
            self.reverse(head, last_node)
            prev_tail.next = last_node
            head.next = next_head

            prev_tail = head
            head = next_head

        return dummy.next

    def split(self, prev_tail, k):
        node = prev_tail
        while k and node:
            node = node.next
            k -= 1

        if node is None:
            return None, None
        
        return node, node.next

    def reverse(self, head, last_node):
        prev_node = None
        curr_node = head
        while prev_node != last_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        

        
