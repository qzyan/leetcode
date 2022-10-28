# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterate over all nodes in the linked list
        # move each node to the head of the linked list
        if head is None:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        curr_node = dummy.next
        while curr_node.next is not None:
            node_to_move = curr_node.next
            curr_node.next = node_to_move.next
            
            node_to_move.next = dummy.next
            dummy.next = node_to_move
            
        
        return dummy.next