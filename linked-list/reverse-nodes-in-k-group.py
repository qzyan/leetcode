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
        prev_node = dummy
        while curr_node:
            tail, next_node = self.split(curr_node, k)
            # last batch, not enough nodes
            if not tail:
                break
            
            new_head = self.reverse(curr_node)
            prev_node.next = new_head
            curr_node.next = next_node

            prev_node = curr_node
            curr_node = next_node

        return dummy.next

    def reverse(self, head):
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        
        return prev_node

    def split(self, node, k):
        while node and k > 1:
            node = node.next
            k -= 1
        
        if node is None:
            return None, None
        
        new_head = node.next
        node.next = None

        return node, new_head
